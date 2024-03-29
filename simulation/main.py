import os
import json
import argparse
import numpy as np
from simulation import simulation, draw_qq_plot, draw_line
from fit import fit, fit_iterate


def main():
    """
    simulate a multi-dimensional hawkes point process, the parameters are hard encoded
    """
    # parse argument
    parser = argparse.ArgumentParser("Multi-dimensional hawkes point process simulator")
    parser.add_argument('params', type=str, nargs='?', default='parameters.json', help="the filepath of json parameter file")
    args = parser.parse_args()

    # load parameters
    parameters = json.load(open(args.params, "rt"))

    # simulate
    U, A, w, T = parameters['U'], parameters['A'], parameters['w'], parameters['T']
    seqs = simulation(U, A, w, T)

    # save result
    dirname = "result"
    os.makedirs(dirname, exist_ok=True)
    json.dump(parameters, open(os.path.join(dirname, "parameters.json"), "wt"), indent=2)
    json.dump(seqs, open(os.path.join(dirname, "sequences.json"), "wt"), indent=2)

    # draw figures
    draw_line(seqs, os.path.join(dirname, "line.svg"))
    draw_qq_plot(parameters, seqs, os.path.join(dirname, "qq_plot.svg"))


main()

