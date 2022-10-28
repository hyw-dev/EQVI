import cv2
import numpy as np
import os

from os.path import isfile, join

def convert_frames_to_video(pathIn,pathOut,fps):
    frame_array = []
    files = [f for f in os.listdir(pathIn) if isfile(join(pathIn, f))]

    # for sorting the file names properly
    # TODO: can be changed depending on your data
    files.sort()
    #print(files)
    #exit()
    print('#####################')
    print(f'Input path: {pathIn}')
    print(f'Total frames: {len(files)}')
    print(f'FPS: {fps}')
    print(f'Output path: {pathOut}')
    print('Processing......')

    for file in files:
        filename = pathIn + file
        #reading each file
        img = cv2.imread(filename)
        height, width, layers = img.shape
        size = (width,height)
        #inserting the frames into an image array
        frame_array.append(img)

    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'mp4v'), fps, size)

    for item in frame_array:
        # writing to a image array
        out.write(item)
    out.release()
    print('Finished!')
    print('#####################')

def main():
    # TODO: change your input & output path here
    pathIn= '/home/yhliu/EQVI_release/outputs/old_films_interp3/1/'
    pathOut = '/home/yhliu/EQVI_release/outputs/old_films_interp3/1_inter3.mp4'

    fps = 25
    convert_frames_to_video(pathIn, pathOut, fps)

if __name__=="__main__":
    main()