import json
import os
import shutil
import argparse

import requests

temp_dir = "temp_dl"

def main(source, query_string, output_file):

    url = source + "/seg-71-v1-a1.ts?" + query_string

    response = requests.get(url)

    if response.status_code !=200:
        print("Query strings like Signature and Policy might have expired OR you don't have access to video")
        exit()

    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    count = 1
    fileList = []
    print("Downloading video segments")
    while response.status_code == 200:
        curr_seg = f"/seg-{count}-v1-a1.ts?"
        response = requests.get(source + curr_seg + query_string)
        with open(temp_dir + curr_seg, 'wb') as f:
            f.write(response.content)
        fileList.append(temp_dir + curr_seg)
        count += 1

    if os.path.getsize(fileList[-1]) < 1000:
        os.remove(fileList[-1])
        fileList = fileList[:-1]

    print("stiching video segments")
    with open(output_file, 'wb') as stitched:
        for filename in fileList:
            with open(os.path.join("", filename), 'rb') as part:
                shutil.copyfileobj(part, stitched)

    #cleanup downloaded files
    for filename in fileList:
        os.remove(filename)
    if len(os.listdir(temp_dir)) == 0:
        os.removedirs(temp_dir)

    print("Done - o ti pari")


if __name__ == "__main__":
    
     parser = argparse.ArgumentParser(description='Download and stitch private kaltura videos')
     parser.add_argument('-src', action='store', dest='src', default=None, help='URL ending in .../a.mp4')
     parser.add_argument('-qstr', action='store', dest='qstr', default=None, help="everything after the '.../seg-xx-v1-a1.ts?'" )
     parser.add_argument('-output', action='store', dest='output', default=None, help='Output file name')

     args = parser.parse_args()
     main(args.src, args.qstr, args.output)



