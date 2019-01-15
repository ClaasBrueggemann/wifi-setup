#!/usr/bin/env python3

import subprocess

def parse_cells(text):
    cells = []
    cell = {}
    for line in text.splitlines():
        cells.append(line)
    return cells


def print_cells(cells):
    for cell in cells:
        print(cell)

def main():
    p = subprocess.run(['nmcli','-f', 'SSID', 'dev', 'wifi', 'list'], stdout=subprocess.PIPE)
    cells = parse_cells(p.stdout.decode('utf-8'))
    print_cells(cells)


if __name__ == '__main__':
    main()