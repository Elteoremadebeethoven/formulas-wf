from manimlib.imports import *
from io import *

FILE = "quadratic"
TEX_CLASS = TexMobject

formula_file = open(f"FORMULAS/TXT/{FILE}.txt","r")
formula_file = formula_file.readlines()

class TransformAnimationFormula(Scene):
    def construct(self):
        self.import_formulas()
        self.write_formulas()
        self.set_changes()
        self.count = 1
        # STEP 1
        self.step_formula(
            fade=(	9,	)
        )
        # STEP 2
        self.step_formula(
            pre_copy=(0,),
            pos_copy=(11,),
            pos_write=(	4,	10,	),
        )
        # STEP 3
        self.step_formula(
            pos_write=(	7,	8,	9,	10,	11,	12,	13,	14,	20,	21,	22,	23,	24,	25,	26,	27,	)
        )
        # STEP 4
        self.step_formula()
        # STEP 5
        self.step_formula(
            fade=(	15,	20,	),
            pre_copy=(	21,	),
            pos_copy=(	20,	)
        )
        # STEP 6
        self.step_formula(
            fade=(	14,	)
        )
        # STEP 7
        self.step_formula(
            pos_write=(	17,	20,	),
        )
        # STEP 8
        self.step_formula(
            pos_write=(	18,	23	),
        )
        # STEP 9
        self.step_formula()
        # STEP 10
        self.step_formula(
            pos_write=(	0,	1,	12,	13,	14,	)
        )
        # STEP 11
        self.step_formula(
            fade=(	0,	1,	2,	9,	10,	),
        )
        # STEP 12
        self.step_formula()
        # STEP 13
        self.step_formula(
            fade=(19,)
        )
        # STEP 14
        self.step_formula()

        self.wait(2)

    def import_formulas(self):
        self.formulas = VGroup(*[
            TEX_CLASS(f)[0] for f in formula_file
        ])
        self.formulas.scale(2)


    def write_formulas(self):
        self.play(Write(self.formulas[0]))

    def set_changes(self):
        self.set_of_changes=[
# STEP 1
[[
(	0,	1,	2,	3,	4,	5,	6,	8,	7,	),
(	0,	1,	2,	3,	4,	5,	7,	6,	8,	)
]],
# STEP 2
[[
(	0,	1,	2,	3,	4,	5,	6,	7,	8,	),
(	5,	0,	1,	2,	3,	6,	7,	8,	9,	)
]],
# STEP 3
[[
(	0,	1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	),
(	0,	1,	2,	3,	4,	5,	6,	15,	16,	17,	18,	19,	)
]],
# STEP 4
[[
(	0,	1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,	25,	26,	27,	),
(	1,	8,	2,	3,	4,	6,	1,	2,	0,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	)
]],
# STEP 5
[[
(	0,	1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	16,	17,	18,	19,	21,	),
(	0,	1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	17,	18,	19,	16,	)
]],
# STEP 6
[[
(	0,	1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	15,	16,	17,	18,	19,	20,	),
(	0,	1,	2,	3,	4,	5,	6,	7,	8,	9,	16,	17,	18,	19,	10,	11,	12,	13,	14,	15,	)
]],
# STEP 7
[[
(	0,	1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	),
(	0,	1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	18,	19,	21,	)
]],
# STEP 8
[[
(	0,	1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	),
(	0,	1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	19,	20,	21,	22,	)
]],
# STEP 9
[[
(	0,	1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	20,	21,	22,	23,	16,	17,	18,	19,	),
(	0,	1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	16,	17,	18,	19,	16,	17,	18,	19,	12,	13,	14,	15,	)
]],
# STEP 10
[[
(	0,	1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	),
(	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,	)
]],
# STEP 11
[[
(	3,	4,	5,	6,	7,	8,	11,	12,	13,	14,	15,	16,	17,	18,	19,	20,	21,	22,	23,	24,	),
(	0,	1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	)
]],
# STEP 12
[[
(	0,	1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	),
(	0,	2,	3,	4,	5,	6,	1,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	19,	)
]],
# STEP 13
[[
(	0,	1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	),
(	0,	1,	2,	3,	4,	5,	6,	7,	8,	9,	10,	11,	12,	13,	14,	15,	16,	17,	18,	)
]],
# STEP 14
[[
(	0,	1,	2,	3,	4,	5,	6,	16,	17,	18,	7,	8,	9,	10,	11,	12,	13,	14,	15,	),
(	0,	1,	2,	3,	13,	14,	15,	13,	14,	15,	4,	5,	6,	7,	8,	9,	10,	11,	12,	)
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