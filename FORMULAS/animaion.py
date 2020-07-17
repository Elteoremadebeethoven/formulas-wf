from manimlib.imports import *
from io import *

FILE = "quadratic"
TEX_CLASS = TexMobject

formula_file = open(f"FORMULAS/TXT/{FILE}.txt","r")
formula_file = formula_file.readlines()

class SolveGeneralQuadraticEquation(Scene):
    def construct(self):
        self.import_formulas()
        self.write_formulas()
        self.set_changes()
        self.count = 1
        # STEP 1
        self.step_formula()

        self.wait(2)

    def import_formulas(self):
        self.formulas = VGroup(*[
            TEX_CLASS(f)[0] for f in formula_file
        ])


    def write_formulas(self):
        self.play(Write(self.formulas[0]))

    def set_changes(self):
        self.set_of_changes=[
# STEP
[[

]],
        ]

    def step_formula(self,
                            pre_write=[],
                            pos_write=[],
                            pre_fade=[],
                            pos_fade=[],
                            fade=[],
                            write=[],
                            changes=[[]],
                            path_arc=0,
                            n_step=0,
                            pre_copy=[],
                            pos_copy=[],
                            time_pre_changes=0.3,
                            time_pos_changes=0.3,
                            run_time=2,
                            time_end=0.3,
                            pre_order=["w","f"],
                            pos_order=["w","f"]
                            ):
        print(f"step: {self.count}")
        n_step = self.count
        formula_copy=[]
        for c in pre_copy:
            formula_copy.append(self.formulas[n_step-1][c].copy())

        for ani_ in pre_order:
            if len(pre_write)>0 and ani_=="w":
                self.play(*[Write(self.formulas[n_step-1][w])for w in pre_write])
            if len(pre_fade)>0 and ani_=="f":
                self.play(*[FadeOut(self.formulas[n_step-1][w])for w in pre_fade])

        self.wait(time_pre_changes)

        for pre_ind,post_ind in self.set_of_changes[n_step-1]:
            self.play(*[
                ReplacementTransform(
                    self.formulas[n_step-1][i],self.formulas[n_step][j],
                    path_arc=path_arc
                    )
                for i,j in zip(pre_ind,post_ind)
                ],
                *[FadeOut(self.formulas[n_step-1][f])for f in fade if len(fade)>0],
                *[Write(self.formulas[n_step][w])for w in write if len(write)>0],
                *[ReplacementTransform(formula_copy[j],self.formulas[n_step][f])
                for j,f in zip(range(len(pos_copy)),pos_copy) if len(pre_copy)>0
                ],
                run_time=run_time
            )

        self.wait(time_pos_changes)

        for ani_ in pos_order:
            if len(pos_write)>0 and ani_=="w":
                self.play(*[Write(self.formulas[n_step][w])for w in pos_write])
            if len(pos_fade)>0 and ani_=="f":
                self.play(*[FadeOut(self.formulas[n_step][w])for w in pos_fade])
        self.wait(time_end)
        self.count += 1