import argparse

def args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--N_JOBS', default=99)
    parser.add_argument('-c', '--CAP', default=100)
    parser.add_argument('--MAX_COORD', default=100)
    parser.add_argument('--MAX_DIST', default=(100*2**0.5))
    parser.add_argument('--LR', default=3e-4)
    parser.add_argument('--DEPOT_END', default=300)
    parser.add_argument('--SERVICE_TIME', default=10)
    parser.add_argument('--TW_WIDTH', default=30)
    parser.add_argument('--N_ROLLOUT', default=50)
    parser.add_argument('--ROLLOUT_STEPS', default=10)
    parser.add_argument('--N_STEPS', default=100)
    parser.add_argument('--init_T', default=100.0)
    parser.add_argument('--final_T', default=1.0)
    parser.add_argument('--device', default="cuda:0")
    return parser.parse_args()
