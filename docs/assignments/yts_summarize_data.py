#!/usr/bin python3

import pandas as pd
import collections

import pandas as pd
import collections

def convert_shift(s, n):
    return pd.to_numeric(s, errors='coerce') + n

def convert(s, d):
    dtype = None
    for x in d.values():
        if x is not None:
            if isinstance(x, bool):
                if dtype is None:
                    dtype = "boolean"
                else:
                    assert dtype == "boolean"
            elif isinstance(x, int):
                if dtype is None:
                    dtype = "Int64"
                else:
                    assert dtype == "Int64" or dtype == "Float64"
            elif isinstance(x, float):
                if dtype is None or dtype == "Int64":
                    dtype = "Float64"
                else:
                    assert dtype == "Float64"
            elif isinstance(x, str):
                if dtype is None:
                    dtype = "string"
                else:
                    assert dtype == "string"
    is_bytes = False
    for x in s: 
        if x is not None:
            is_bytes = isinstance(x, bytes)
            break
    if is_bytes:
        for x in d:
            if isinstance(x, int):
                try:
                    s = convert_shift(s, 0)
                except:
                    pass
            break
    d = collections.defaultdict(lambda: None, d)
    return pd.Series([ d[k] for k in s ], dtype=dtype)


config = {
        1999 : {
            "file" : "data/nyts1999public.sas7bdat",
            "age" : ("QN1", convert_shift, 8),
            "sex" : ("QN2", convert, { 1: 'F', 2: 'M' }),
            "grade" : ("QN3", convert_shift, 5),
            "ever_smoked" : ("QN6", convert, {1: True, 2: False}),
            "first_age" : ("QN7", convert, {1: None, 2: 8, 3: 9.5, 4: 11.5, 5:13.5, 6:15.5, 7:17}),
            "num_days" : ("QN10", convert, {1: 0, 2: 1.5, 3:4, 4:7.5, 5:14.5, 6:24.5, 7:30}),
            "will_smoke" : ("QN41", convert, {1: True, 2: True, 3: False, 4: False}),
            "harmful" : ("QN68", convert, {1: True, 2: True, 3: False, 4: False}),
        },
        2000 : {
            "file" : "data/nyts2000public.sas7bdat",
            "age" : ("qn1", convert_shift, 8),
            "sex" : ("qn2", convert, { 1: 'F', 2: 'M' }),
            "grade" : ("qn3", convert_shift, 5),
            "ever_smoked" : ("qn8", convert, {1: True, 2: False}),
            "first_age" : ("qn9", convert, {1: None, 2: 8, 3: 9.5, 4: 11.5, 5:13.5, 6:15.5, 7:17}),
            "num_days" : ("qn13", convert, {1: 0, 2: 1.5, 3:4, 4:7.5, 5:14.5, 6:24.5, 7:30}),
            "will_smoke" : ("qn51", convert, {1: True, 2: True, 3: False, 4: False}),
            "harmful" : ("qn79", convert, {1: True, 2: True, 3: False, 4: False}),
        },
        2002 : {
            "file" : "data/nyts2002_final.sas7bdat",
            "age" : ("q1", convert_shift, 8),
            "sex" : ("q2", convert, { 1: 'F', 2: 'M' }),
            "grade" : ("q3", convert_shift, 5),
            "ever_smoked" : ("q7", convert, {1: True, 2: False}),
            "first_age" : ("q9", convert,
                   {1: None, 2: 8, 3: 9, 4: 10, 5: 11, 6: 12, 7:13, 8: 14, 9:15, 10:16, 11:17}
            ),
            "num_days" : ("q12", convert, {1: 0, 2: 1.5, 3:4, 4:7.5, 5:14.5, 6:24.5, 7:30}),
            "will_smoke" : ("q50", convert, {1: True, 2: True, 3: False, 4: False}),
            "harmful" : ("q58", convert, {1: True, 2: True, 3: False, 4: False}),
        },
        2004 : {
            "file" : "data/nyts2004_public_092205.sas7bdat",
            "age" : ("QN1", convert_shift, 8),
            "sex" : ("QN2", convert, { 1: 'F', 2: 'M' }),
            "grade" : ("QN3", convert_shift, 5),
            "ever_smoked" : ("QN8", convert, {1: True, 2: False}),
            "first_age" : ("QN9", convert,
                   {1: None, 2: 8, 3: 9, 4: 10, 5: 11, 6: 12, 7:13, 8: 14, 9:15, 10:16, 11:17}
            ),
            "num_days" : ("QN13", convert, {1: 0, 2: 1.5, 3:4, 4:7.5, 5:14.5, 6:24.5, 7:30}),
            "will_smoke" : ("QN58", convert, {1: True, 2: True, 3: False, 4: False}),
            "harmful" : ("QN52", convert, {1: True, 2: True, 3: False, 4: False}),
        },
        2006 : {
            "file" : "data/2006_Codebook_Dataset_SAS/2006 NYTS SAS Dataset_2008 08-05_FINAL.sas7bdat",
            "age" : ("qn1", convert_shift, 8),
            "sex" : ("qn2", convert, { 1: 'F', 2: 'M' }),
            "grade" : ("qn3", convert_shift, 5),
            "ever_smoked" : ("qn8", convert, {1: True, 2: False}),
            "first_age" : ("qn9", convert,
                           {1: None, 2: 8, 3: 9, 4: 10, 5: 11, 6: 12, 7:13, 8:14, 9:15, 10:16, 11:17}
            ),
            "num_days" : ("qn13", convert, {1: 0, 2: 1.5, 3:4, 4:7.5, 5:14.5, 6:24.5, 7:30}),
            "will_smoke" : ("qn58", convert, {1: True, 2: True, 3: False, 4: False}),
            "harmful" : ("qn52", convert, {1: True, 2: True, 3: False, 4: False}),
        },
        2009 : {
            "file" : "data/2009_Codebook_Dataset_SAS/nyts_2009_dataset.sas7bdat",
            "age" : ("qn1", convert_shift, 8),
            "sex" : ("qn2", convert, { 1: 'F', 2: 'M' }),
            "grade" : ("qn3", convert_shift, 5),
            "ever_smoked" : ("qn8", convert, {1: True, 2: False}),
            "first_age" : ("qn9", convert,
                           {1: None, 2: 8, 3: 9, 4: 10, 5: 11, 6: 12, 7:13, 8:14, 9:15, 10:16, 11:17}
            ),
            "num_days" : ("qn13", convert, {1: 0, 2: 1.5, 3:4, 4:7.5, 5:14.5, 6:24.5, 7:30}),
            "will_smoke" : ("qn58", convert, {1: True, 2: True, 3: False, 4: False}),
            "harmful" : ("qn52", convert, {1: True, 2: True, 3: False, 4: False}),
        },
        2011 : {
            "file" : "data/2011-dataset-codebook-sas/nyts2011.sas7bdat",
            "age" : ("qn1", convert_shift, 8),
            "sex" : ("qn2", convert, { 1: 'F', 2: 'M' }),
            "grade" : ("qn3", convert_shift, 5),
            "ever_smoked" : ("qn7", convert, {1: True, 2: False}),
            "ever_vaped" : ("qn36h", convert, {1: True}),
            # Note: in this year, question switches to "one or two puffs" from "whole cig"
            "first_age" : ("qn11", convert,
                           {1: None, 2: 8, 3: 9, 4: 10, 5: 11, 6: 12, 7:13, 8: 14, 9:15, 10:16, 11:17, 12:18, 13:19}
            ),
            "num_days" : ("qn13", convert, {1: 0, 2: 1.5, 3:4, 4:7.5, 5:14.5, 6:24.5, 7:30}),
            "will_smoke" : ("qn8", convert, {1: True, 2: True, 3: False, 4: False}),
            "harmful" : ("qn72", convert, {1: True, 2: True, 3: False, 4: False}),
        },
        2012 : {
            "file" : "data/2012-codebook-dataset-sas/nyts2012.sas7bdat",
            "age" : ("qn1", convert_shift, 8),
            "sex" : ("qn2", convert, { 1: 'F', 2: 'M' }),
            "grade" : ("qn3", convert_shift, 5),
            "ever_smoked" : ("qn7", convert, {1: True, 2: False}),
            "ever_vaped" : ("qn37g", convert, {1: True}),
            "first_age" : ("qn11", convert,
                           {1: None, 2: 8, 3: 9, 4: 10, 5: 11, 6: 12, 7:13, 8: 14, 9:15, 10:16, 11:17, 12:18, 13:19}
            ),
            "num_days" : ("qn13", convert, {1: 0, 2: 1.5, 3:4, 4:7.5, 5:14.5, 6:24.5, 7:30}),
            "will_smoke" : ("qn8", convert, {1: True, 2: True, 3: False, 4: False}),
            "harmful" : ("qn75", convert, {1: False, 2: False, 3: True, 4: True}),
        },
        2013 : {
            "file" : "data/2013-codebook-dataset-sas/nyts2013.sas7bdat",
            "age" : ("qn1", convert_shift, 8),
            "sex" : ("qn2", convert, { 2: 'F', 1: 'M' }),
            "grade" : ("qn3", convert_shift, 5),
            "ever_smoked" : ("qn9", convert, {1: True, 2: False}),
            "ever_vaped" : ("qn36i", convert, {1: True}),
            "first_age" : ("qn13", convert,
                           {1: None, 2: 8, 3: 9, 4: 10, 5: 11, 6: 12, 7:13, 8: 14, 9:15, 10:16, 11:17, 12:18, 13:19}
            ),
            "num_days" : ("qn15", convert, {1: 0, 2: 1.5, 3:4, 4:7.5, 5:14.5, 6:24.5, 7:30}),
            # Note: this is "will smoke cig" but also has "will smoke tobacco"
            "will_smoke" : ("qn10", convert, {1: True, 2: True, 3: False, 4: False}),
            "harmful" : ("qn71", convert, {1: False, 2: False, 3: True, 4: True}),
        },
        2014 : {
            "file" : "data/2014-dataset-codebook-sas/nyts2014.sas7bdat",
            "age" : ("qn1", convert_shift, 8),
            "sex" : ("qn2", convert, { 2: 'F', 1: 'M' }),
            "grade" : ("qn3", convert_shift, 5),
            "ever_smoked" : ("qn7", convert, {1: True, 2: False}),
            "ever_vaped" : ("qn31", convert, {1: True, 2: False}),
            "first_age" : ("qn11", convert,
                           {1: None, 2: 8, 3: 9, 4: 10, 5: 11, 6: 12, 7:13, 8: 14, 9:15, 10:16, 11:17, 12:18, 13:19}
            ),
            "num_days" : ("qn13", convert, {1: 0, 2: 1.5, 3:4, 4:7.5, 5:14.5, 6:24.5, 7:30}),
            "will_smoke" : ("qn8", convert, {1: True, 2: True, 3: False, 4: False}),
            "harmful" : ("qn63", convert, {1: False, 2: False, 3: True, 4: True}),
        },
        2015 : {
            "file" : "data/2015-dataset-codebook-sas/nyts2015.sas7bdat",
            "age" : ("q1", convert_shift, 8),
            "sex" : ("q2", convert, { 2: 'F', 1: 'M' }),
            "grade" : ("q3", convert_shift, 5),
            "ever_smoked" : ("q6", convert, {1: True, 2: False}),
            "ever_vaped" : ("q28", convert, {1: True, 2: False}),
            "first_age" : ("q10", convert,
                           {1: None, 2: 8, 3: 9, 4: 10, 5: 11, 6: 12, 7:13, 8: 14, 9:15, 10:16, 11:17, 12:18, 13:19}
            ),
            "num_days" : ("q12", convert, {1: 0, 2: 1.5, 3:4, 4:7.5, 5:14.5, 6:24.5, 7:30}),
            "will_smoke" : ("q7", convert, {1: True, 2: True, 3: False, 4: False}),
            "harmful" : ("q61", convert, {1: False, 2: False, 3: True, 4: True}),
        },
        2016 : {
            "file" : "data/2016-dataset-codebook-sas/nyts2016.sas7bdat",
            "age" : ("Q1", convert_shift, 8),
            "sex" : ("Q2", convert, { 2: 'F', 1: 'M' }),
            "grade" : ("Q3", convert_shift, 5),
            "ever_smoked" : ("Q7", convert, {1: True, 2: False}),
            "ever_vaped" : ("Q26", convert, {1: True, 2: False}),
            "first_age" : ("Q11", convert,
                           {1: None, 2: 8, 3: 9, 4: 10, 5: 11, 6: 12, 7:13, 8: 14, 9:15, 10:16, 11:17, 12:18, 13:19}
            ),
            "num_days" : ("Q13", convert, {1: 0, 2: 1.5, 3:4, 4:7.5, 5:14.5, 6:24.5, 7:30}),
            "will_smoke" : ("Q9", convert, {1: True, 2: True, 3: False, 4: False}),
        },
        2017 : {
            "file" : "data/2017-dataset-codebook-sas/nyts2017.sas7bdat",
            "age" : ("Q1", convert_shift, 8),
            "sex" : ("Q2", convert, { 2: 'F', 1: 'M' }),
            "grade" : ("Q3", convert_shift, 5),
            "ever_smoked" : ("Q7", convert, {1: True, 2: False}),
            "ever_vaped" : ("Q28", convert, {1: True, 2: False}),
            "first_age" : ("Q8", convert,
                           {1: None, 2: 8, 3: 9, 4: 10, 5: 11, 6: 12, 7:13, 8: 14, 9:15, 10:16, 11:17, 12:18, 13:19}
            ),
            "num_days" : ("Q11", convert, {1: 0, 2: 1.5, 3:4, 4:7.5, 5:14.5, 6:24.5, 7:30}),
            "will_smoke" : ("Q16", convert, {1: True, 2: True, 3: False, 4: False}),
        },
        2018 : {
            "file" : "data/2018-nyts-dataset-codebook-sas/nyts2018.sas7bdat",
            "age" : ("Q1", convert_shift, 8),
            "sex" : ("Q2", convert, { 2: 'F', 1: 'M' }),
            "grade" : ("Q3", convert_shift, 5),
            "ever_smoked" : ("Q7", convert, {1: True, 2: False}),
            "ever_vaped" : ("Q28", convert, {1: True, 2: False}),
            "first_age" : ("Q8", convert,
                           {1: None, 2: 8, 3: 9, 4: 10, 5: 11, 6: 12, 7:13, 8: 14, 9:15, 10:16, 11:17, 12:18, 13:19}
            ),
            "num_days" : ("Q11", convert, {1: 0, 2: 1.5, 3:4, 4:7.5, 5:14.5, 6:24.5, 7:30}),
            "will_smoke" : ("Q16", convert, {1: True, 2: True, 3: False, 4: False}),
            "harmful" : ("Q73", convert, {1: False, 2: False, 3: True, 4: True}),
        },
        2019 : {
            "file" : "data/2019-nyts-dataset-and-codebook-sas/nyts2019.sas7bdat",
            "age" : ("Q1", convert_shift, 8),
            "sex" : ("Q2", convert, { 2: 'F', 1: 'M' }),
            "grade" : ("Q3", convert_shift, 5),
            "ever_smoked" : ("Q6", convert, {1: True, 2: False}),
            "ever_vaped" : ("Q34", convert, {1: True, 2: False}),
            "first_age" : ("Q7", convert,
                           {1: 8, 2: 9, 3: 10, 4: 11, 5: 12, 6: 13, 7:14, 8: 15, 9:16, 10:17, 11:18, 12:19}
            ),
            "num_days" : ("Q9", convert, {k:k for k in range(31)}),
            "will_smoke" : ("Q16", convert, {1: True, 2: True, 3: False, 4: False}),
            "harmful" : ("Q87", convert, {1: False, 2: False, 3: True, 4: True}),
        },
}


dfs = []
vnames = ['ever_smoked', 'ever_vaped', 'first_age', 'num_days', 'will_smoke', 'harmful']

for k in config:
    yts = pd.read_sas(config[k]['file']).convert_dtypes()
    df = {}
    for n, v in config[k].items():
        if n == "file":
            continue
        col, fn, args = v
        df[n] = fn(yts[col], args)
    # post-process 'ever_vaped' since in some years this has NA for everything except True's
    if 'ever_vaped' not in df:
        df['ever_vaped'] = False
    elif len(config[k]['ever_vaped'][2]) == 1:
        vape = df['ever_vaped']
        df['ever_vaped'] = vape.mask(~vape, False)
    if 'harmful' not in df:
        df['harmful'] = pd.NA
    out = pd.DataFrame(df).groupby(['grade', 'sex'])[vnames].agg(
        n = ('ever_smoked', 'size'),
        p_cig = ('ever_smoked', 'mean'),
        p_vape = ('ever_vaped', 'mean'),
        first_age = ('first_age', 'mean'),
        num_days = ('num_days', 'mean'),
        p_will_smoke = ('will_smoke', 'mean'),
        p_harmful = ('harmful', 'mean'),
    )
    out['year'] = k
    out.reset_index()
    dfs.append(out)

everything = pd.concat(dfs)

everything.to_csv("yts_summarized.csv")
