import os
import yaml
import re
import pprint

pp = pprint.PrettyPrinter(indent=4)
def parse_filetypes_yaml(filetypes_path):
    with open(filetypes_path, 'r') as file:
        filetypes_data = yaml.load(file)

    config = filetypes_data['config']
    rules = filetypes_data['rules']

    rule_groups = {}
    for rule_name in rules:
        if 'patterns' in rules[rule_name]:
            if 'gpri' not in rules[rule_name]:
                rules[rule_name]['gpri'] = 0
            rule_groups[rule_name] = rules[rule_name]
            '''
            if 'skips' in rules[rule_name]:
                rules['skips'].extend(rules[rule_name]['skips'])
                rules[rule_name].pop('skips')
            '''
            print('Group:', rule_name, '\n', rules[rule_name])
        if rule_name == 'skips':
            skips = []
            for subitem in rules['skips']:
                if isinstance(subitem, list):
                    for item in subitem:
                        skips.append(item)
                else:
                    skips.append(subitem)

            print('Skipped filetypes:\n', skips)

    sorted_groups = sorted(rule_groups, key=lambda x: (rule_groups[x]['gpri']),reverse=True)
    print(sorted_groups)


parse_filetypes_yaml('filetypes.yaml')
