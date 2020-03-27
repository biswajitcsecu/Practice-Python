
from __future__ import  print_function
import sys, os
import imgui


def main():
    try:

        # initilize imgui context (see documentation)
        imgui.create_context()
        imgui.get_io().display_size = 100, 100
        imgui.get_io().fonts.get_tex_data_as_rgba32()

        # start new frame context
        imgui.new_frame()

        # open new window context
        imgui.begin("Your first window!", True)

        # draw text label inside of current window
        imgui.text("Hello world!")

        # close current window context
        imgui.end()

        # pass all drawing comands to the rendering pipeline
        # and close frame context
        imgui.render()
        imgui.end_frame()


    except ModuleNotFoundError:
        print("Error found")



if __name__=="__main__":
    main()