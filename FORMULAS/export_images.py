from manimlib.imports import *
from io import *

# OPTIONS
FILE = "quadratic"
TEX_CLASS = TexMobject

SCALE = 0.016
NUMBER_DIRECTION = DOWN
NUMBER_BUFF = 0.01
FORMULA_NUMBER_HEIGHT = 0.7
# DON'T MODIFY
TXT_FOLDER = "TXT"
IMAGE_TEX_DIR = "IMAGES"
FILE_UPPER = FILE.upper()
FILE_JOIN = f"FORMULAS/{FILE_UPPER}"
for file_path in [FILE_JOIN, f"{FILE_JOIN}/{IMAGE_TEX_DIR}"]:
    if not os.path.exists(file_path):
        os.makedirs(file_path)

formula_file = open(f"FORMULAS/{TXT_FOLDER}/{FILE}.txt","r")
formula_file = formula_file.readlines()

class PrintTeX(Scene):
    CONFIG = {
        "color_cycle": [RED, BLUE, YELLOW, TEAL_D, PURPLE, PINK]
    }
    def construct(self):
        texs = VGroup(*[
            TEX_CLASS(f) for f in formula_file
        ])
        count = 1
        for tex in texs:
            self.scale_tex(tex)
            formula_number = Text(f"{count}",font="Arial",stroke_width=0)\
                .set_height(FORMULA_NUMBER_HEIGHT)
            formula_number.to_edge(DOWN)
            sub_numbers = self.get_sub_numbers(tex)
            self.add(tex,sub_numbers,formula_number)
            self.update_frame(ignore_skipping=True)
            self.get_image().save(f"{FILE_JOIN}/{IMAGE_TEX_DIR}/im_{count}.png","PNG")
            self.update_frame(ignore_skipping=False)
            self.remove(tex,sub_numbers,formula_number)
            count += 1

    def scale_tex(self, tex):
        tex_ratio = tex.get_width() / tex.get_height()
        if tex_ratio < 16/9:
            tex.set_height(FRAME_HEIGHT - 0.7)
        else:
            tex.set_width(FRAME_WIDTH - 0.7)

    def get_sub_numbers(self, tex):
        sub_numbers = VGroup()
        tex_ratio = tex.get_width() / tex.get_height()
        for t in tex:
            count = 0
            colors = it.cycle(self.color_cycle)
            for sub_t in t:
                color = next(colors)
                n = Text(f"{count}", font="Arial",stroke_width=0)
                if tex_ratio < 1:
                    n.set_width(tex.get_width() * SCALE)
                else:
                    n.set_height(tex.get_width() * SCALE)

                #n.set_height(sub_t.get_height()*SCALE)
                n.next_to(sub_t, NUMBER_DIRECTION, NUMBER_BUFF)
                VGroup(sub_t,n).set_color(color)
                sub_numbers.add(n)
                count += 1
        return sub_numbers
