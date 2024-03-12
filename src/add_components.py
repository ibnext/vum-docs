#!/usr/bin/env python3

import os
import sys
import json
import argparse

import yaml

"""
    We have cases where, deep down in the structure, there are
    differences between werkzoekendenProfielen and Vacatures.

    We handle these by adding a suffix:
        _V: Vacature interface
        _W: Werkzoekende interface
        _VUM: interface hosted by VUM
        _BRN: interface hosted by Bron
    Keys that have a suffix are inserted without the suffix 
    only in the appropriate domain.

    The domain is determined based on the name of the file.

    Relevant keys are:
        - names of referenced schemas
        - names of properties
        - required properties

"""

POSTFIXES = [
        "_V",
        "_W",
        "_VUM",
        "_BRN"
    ]

def match_postfix(key, postfixes):
    for pf in postfixes:
        if key.endswith(pf):
            return key[:-len(pf)]
    return ""

def preprocess_components(instance, postfixes):
    if isinstance(instance, dict):
        for (key, value) in instance.items():
            if key == "properties":
                for (propname, schema) in list(value.items()):
                    prefix = match_postfix(propname, postfixes)
                    if prefix:
                        value[prefix] = schema
                for (propname, schema) in list(value.items()):
                    prefix = match_postfix(propname, POSTFIXES)
                    if prefix:
                        del value[propname]
            if key == "required" and isinstance(value, list):
                for propname in list(value):
                    prefix = match_postfix(propname, postfixes)
                    if prefix:
                        value.append(prefix)
                for propname in list(value):
                    prefix = match_postfix(propname, POSTFIXES)
                    if prefix:
                        value.remove(propname)
            preprocess_components(value, postfixes)
    elif isinstance(instance, list):
        for value in instance:
            preprocess_components(value, postfixes)

def json_walk(instance, path=[]):
    if isinstance(instance, dict):
        for (key, value) in instance.items():
            if key == "$ref" and value.startswith("#/components"):
                yield value
            else:
                _path = list(path)
                _path.append(key)
                yield from json_walk(value, _path)
    elif isinstance(instance, list):
        for value in instance:
            yield from json_walk(value, path)

def cleanup_components(openapi):
    deletes = True
    while deletes:
        deletes = False
        references = [ref.split("/")[2:] for ref in json_walk(openapi)]
        for (section, content) in list(openapi["components"].items()):
            for key in list(content.keys()):
                path = [section, key]
                if path not in references:
                    content.pop(key)
                    deletes = True

    # Check that all remaining references can be resolved
    references = [ref.split("/")[1:] for ref in json_walk(openapi)]
    for ref in references:
        openapi[ref[0]][ref[1]][ref[2]]
    print("Referenties opgeschoond en gecontroleerd.")

def main(components_file, openapi_file, output_directory):
    with open(components_file) as fd:
        components = yaml.load(fd, Loader=yaml.Loader)
    with open(openapi_file) as fd:
        openapi = yaml.load(fd, Loader=yaml.Loader)

    postfixes = []
    if "Werkzoekende" in openapi_file:
        postfixes.append("_W")
    if "Vacature" in openapi_file:
        postfixes.append("_V")
    if "Bron" in openapi_file:
        postfixes.append("_BRN")
    if "Bemiddelaar" in openapi_file:
        postfixes.append("_VUM")

    preprocess_components(components, postfixes)

    openapi["components"] = components["components"]
    cleanup_components(openapi)

    filename, _ = os.path.splitext(os.path.basename(openapi_file))
    yaml_filename = os.path.join(output_directory, filename+".yaml")
    json_filename = os.path.join(output_directory, filename+".json")

    print(f"Saving to {json_filename}")
    with open(json_filename, 'w') as fd:
        json.dump(openapi, fd, indent=2)
    print(f"Saving to {yaml_filename}")
    with open(yaml_filename, 'w') as fd:
        yaml.dump(openapi, fd, Dumper=yaml.Dumper, sort_keys=False)

def options():
    arg_parser = argparse.ArgumentParser(
        description='Add the components definition section to the '
                    'yaml files for the interface.')
    arg_parser.add_argument(
        '-c', 
        dest='components_file', 
        required=False, 
        default="components.yaml"
    )
    arg_parser.add_argument(
        '-f', 
        dest='openapi_file', 
        required=True
    )
    arg_parser.add_argument(
        '-o', 
        dest='output_directory', 
        required=True
    )
    return vars(arg_parser.parse_args(sys.argv[1:]))


if __name__ == '__main__':
    main(**options())

