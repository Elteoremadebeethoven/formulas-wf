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
                            pos_write=[],
                            pre_fade=[],
                            fade=[],
                            write=[],
                            pre_copy=[],
                            pos_copy=[],
                            time_pre_changes=0.3,
                            time_pos_changes=0.3,
                            run_time=2,
                            time_end=0.3,
                            ):
        print(f"step: {self.count}")
        n_step = self.count
        formula_copy=[]

        pre_formula = self.formulas[n_step - 1]
        pos_formula = self.formulas[n_step]

        for c in pre_copy:
            formula_copy.append(pre_formula[c].copy())

        if len(pre_fade) > 0:
            self.play(*[
                FadeOut(pre_formula[w])
                for w in pre_fade
            ])

        self.wait(time_pre_changes)

        for pre_ind,post_ind in self.set_of_changes[n_step-1]:
            self.play(
                *[
                    ReplacementTransform(
                        pre_formula[i],pos_formula[j],
                    )
                    for i,j in zip(pre_ind,post_ind)
                ],
                *[
                    FadeOut(pre_formula[f])
                    for f in fade
                ],
                *[
                    Write(pos_formula[w])
                    for w in write
                ],
                *[
                    ReplacementTransform(
                        formula_copy[j],
                        pos_formula[f]
                    )
                    for j,f in zip(
                                    range(len(pos_copy)),
                                    pos_copy
                                )
                ],
                run_time=run_time
            )

        self.wait(time_pos_changes)
        
        if len(pos_write) > 0:
            self.play(*[
                Write(pos_formula[w])
                for w in pos_write
            ])

        self.wait(time_end)
        self.count += 1
