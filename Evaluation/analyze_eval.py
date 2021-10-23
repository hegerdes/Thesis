import pandas as pd
pd.options.mode.chained_assignment = None

def win_raw(df: pd.DataFrame):
    df = df[df['ProcessName'].isin(['node', 'mysqld', 'sqlwriter', 'xampp-control'])]

    print('######WIN_RAW######')
    for pid,df_pid in df.groupby("ProcessName"):
        print('{:18}{:8.4f}\t{:8.4f}\t{:10.4f}'.format(pid, df_pid['CPU(s)'].median(), df_pid['CPU(s)'].mean(), df_pid['WS(M)'].mean()))
    print()

def win_docker(df: pd.DataFrame):
    df = df[df['ProcessName'].isin(['com.docker.backend', 'com.docker.dev-envs', 'com.docker.proxy','docker', 'com.docker.service', 'com.docker.wsl-distro-proxy', 'DockerDesktop', 'vmmem', 'wsl', 'vmcompute', 'vpnkit', 'vpnkit-bridge'])]

    print('#####WIN_DOCKER#####')
    for pid,df_pid in df.groupby("ProcessName"):
        print('{:18}{:8.4f}\t{:8.4f}\t{:10.4f}'.format(pid.replace('com.','').replace('distro-',''), df_pid['CPU(s)'].median(),df_pid['CPU(s)'].mean(), df_pid['WS(M)'].mean()))
    print()

def linux_raw(df: pd.DataFrame):
    df = df[df['COMMAND'].isin(['npm', 'node', 'mariadbd' ])]
    df['RES'] = df['RES'].div(1024, axis=0)

    print('#####UNIX_RAW#####')
    for pid,df_pid in df.groupby("COMMAND"):
        print('{:18}{:8.4f}\t{:8.4f}\t{:10.4f}'.format(pid.replace('com.','').replace('distro-',''), df_pid['%CPU'].median(), df_pid['%CPU'].mean(), df_pid['RES'].mean()))
    print()

def linux_docker(df: pd.DataFrame):
    df = df[df['COMMAND'].isin(['npm', 'node', 'mysqld', 'docker-proxy', 'dockerd', 'docker-driver', 'containerd-shim'])]
    df['RES'] = df['RES'].div(1024)

    print('#####UNIX_DOCKER#####')
    for pid,df_pid in df.groupby("COMMAND"):
        print('{:18}{:8.4f}\t{:8.4f}\t{:10.4f}'.format(pid.replace('com.','').replace('distro-',''), df_pid['%CPU'].median(), df_pid['%CPU'].mean(), df_pid['RES'].mean()))
    print()

def win_docker_stats(df: pd.DataFrame):
    df['CPUPerc'] = df['CPUPerc'].str.replace('%', '')
    df['CPUPerc'] = df['CPUPerc'].astype(float)

    df[['MemUsed', 'MemAvil']] = df['MemUsage'].str.split('/', 1, expand=True)
    df['MemUsed'] = df['MemUsed'].str.replace('MiB', '')
    df['MemUsed'] = df['MemUsed'].astype(float)

    print('#####DOCKER_STATS#####')
    for pid,df_pid in df.groupby("Name"):
        print('{:18}{:8.4f}\t{:8.4f}\t{:10.4f}'.format(pid, df_pid['CPUPerc'].mean(), df_pid['CPUPerc'].median(), df_pid['MemUsed'].mean()))
    print()


if __name__ == '__main__':

    # WIN READ
    df_win_raw = pd.read_csv("Evaluation/stats_win_raw.csv", delim_whitespace=True, decimal=",", thousands='.')
    df_win_docker = pd.read_csv("Evaluation/stats_win_docker.csv", delim_whitespace=True, decimal=",", thousands='.')
    df_win_docker_stats = pd.read_csv("Evaluation/stats_win_docker.txt", delimiter='\t')

    # UNIX READ
    df_linux_raw = pd.read_csv("Evaluation/stats_linux_raw.csv", delim_whitespace=True, decimal=".")
    df_linux_docker = pd.read_csv("Evaluation/stats_linux_docker.csv", delim_whitespace=True, decimal=".")
    df_linux_docker_stats = pd.read_csv("Evaluation/stats_linux_docker.txt", delimiter='\t')


    # WIN CALC
    win_raw(df_win_raw)
    win_docker(df_win_docker)
    win_docker_stats(df_win_docker_stats)

    # UNIX CALC
    linux_raw(df_linux_raw)
    linux_docker(df_linux_docker)
    win_docker_stats(df_linux_docker_stats)


    print(sum([16.4034, 52.4844, 13.7308, 103.0627]))
