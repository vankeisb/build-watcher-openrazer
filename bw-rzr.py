#!/usr/bin/env python3

import openrazer.client
import os
import json


color_green = (0,255,0)
color_red = (255,0,0)
color_orange = (255,255,0)
color_black = (0,0,0)

home = os.environ.get('HOME')
dataFilePath = home + "/.build-watcher-data.json"

with open(dataFilePath, 'r') as dataFile:
    data = dataFile.read()
    # Parse the JSON data
    try:
        j = json.loads(data, "utf-8")
        tags = j["tags"]
        index = 0

        mgr = openrazer.client.DeviceManager()
        device = mgr.devices[0]

        rows, cols = device.fx.advanced.rows, device.fx.advanced.cols
        for row in range(rows):
            # fn keys start at 2
            for col in range(2, cols):
                color = color_black
                if index < len(tags):
                    tag = tags[index]
                    print(tag)
                    status = tag["status"]
                    if status == "Green":
                        color = color_green
                    elif status == "Red":
                        color = color_red
                    else:
                        color = color_orange

                device.fx.advanced.matrix[row,col] = color
                print(row, ',', col, ':', color)
                index = index + 1

        device.fx.advanced.draw()

    except ValueError:
        print("Json decoding failed : " + data)