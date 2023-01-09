# SLURM Job Scheduling

Simple Linux Utility for Resource Management, used to manage resources (CPU cores/threads, memory, interconnect (MPI), GPUs, etc.) and job scheduling (different scheduler such as for different users, groups, or priority based). 

## Job Allocation 
```sh
sbatch # submit a script for later execution (batch mode)
salloc # create job allocation and start a shell (interactive mode)
srun # create job allocation and launch a job step
sattach # attach stdio to an existing job
```

### Common Argument Options
Some commonly used argument for `sbatch` and `srun`

```sh
-J, --job-name=<jobname> 
# Specify a name for the job

-n, --ntasks=<number>
# number of tasks will run, so that slurm allocates
# enough resources for all the tasks. 

-c, --cpus-per-task=<n> 
# number of CPUs per process, default is 1

--mem=<size>[K|M|G|T] 
# the size of memory required per node, default unit in Mb

-q, --qos=<qos> 
# request a quality of service for the job.
# use the following command to show all qos set by admin
sacctmgr show qos format=name,priority

-t, --time=<time> # set a limit to the total running time 
# by SIGTERM and SIGKILL. Acceptable time formats include 
# "mm", "mm:ss", "hh:mm:ss", 
# "days-hh", "days-hh:mm" and "days-hh:mm:ss".

-p, --partition=<partition_names> 
# request a specific partition for the resource allocation. 

-i, --input=<filename_pattern>
-o, --output=<filename_pattern>
-e, --error=<filename_pattern>
# Specify the "filename pattern" for stdin/out/err redirection. 

-G, --gpus=[type:]<number>
# the total number of GPUs required for the job. 
# An optional GPU type specification can be supplied. 
```


### `srun`
```sh
srun [OPTIONS ... [executable [args ...]]]
```

Run a parallel job on cluster managed by Slurm. If necessary, srun will first create a resource allocation in which to run the parallel job.

`srun` is interactive and **blocking**

Compared to `sbatch`, often consider adding

```sh
--pty # Execute task zero in pseudo terminal mode. 
```

Simple example
```sh
$> srun -mem 20M echo helloworld
helloworld

$> srun -mem 20M --pty bash
cpu0 $> # running bash on the allocated process
```

### `sbatch` and sbatch script

```sh
sbatch [OPTIONS(0)...] [ : [OPTIONS(N)...]] script [args(0)...]
```
sbatch submits a batch script to slurm and returns after the task script is submitted to slurm. 

The batch script may be given to `sbatch` through a file name on the command line, or if no file name is specified, `sbatch` will read in a script from standard input. 

The batch script may contain options preceded with `#SBATCH` before any executable commands in the script. `sbatch` will stop processing further #SBATCH directives once the first non-comment non-whitespace line has been reached in the script.

Simple example
```sh
$> cat script.slrm
#!/bin/bash
#SBATCH --job-name=train
#SBATCH --output=output.log
#SBATCH -n 1
echo helloworld

$> sbatch script.slrm
Submitted batch job XXXXXXX

$> cat output.log
helloworld
```

### Filename Pattern
For redirected out/err files, we could use the following pattern replacement.

```sh
%j # jobid of the running job.
%u # User name.
%x # Job name.
```

## Examples

Submitting a NN training job using python and pytorch
```sh
#!/bin/bash
#SBATCH --job-name=train
#SBATCH -c 4
#SBATCH --mem=16G
#SBATCH --time=24:00:00
#SBATCH --output=result_%j.log
pwd; hostname; date
python train.py
date
```

Submitting an OMP job
```sh
#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8
#SBATCH --time=00:10:00
#SBATCH --job-name=omp
#SBATCH --output=omp_%j.out

executable
```

Submitting a MPI job

```sh
#!/bin/bash
#SBATCH --nodes=1
#SBATCH --ntasks=16
#SBATCH --cpus-per-task=1
#SBATCH --time=1:00:00
#SBATCH --job-name=mpi
#SBATCH --output=mpi_%j.out

executable
```

## `sinfo` 

```sh
sinfo [OPTIONS...]  
```
view partition and node information for a system running Slurm.

Some commonly used options 

```sh
-l, --long
# Print more detailed information.

-N, --Node
# Print information in a node-oriented format 
# with one line per node and partition. 

-e, --exact
# If set, do not group node information on multiple nodes 
# unless their configurations to be reported are identical. 

-n, --nodes=<nodes>
# Print information about the specified node(s). 
# Multiple nodes may be comma separated or expressed using a node range 
# expression (e.g. "linux[00-17]").

-p, --partition=<partition>
# Print information only about the specified partition(s). 
# Multiple partitions are separated by commas.
```

For Example
```
$> sinfo -lNe -p p100
NODELIST   NODES PARTITION       STATE CPUS    S:C:T MEMORY TMP_DISK WEIGHT AVAIL_FE REASON
gpu001         1      p100       mixed 32      2:8:2 172000        0      1     P100 none
gpu002         1      p100    drained* 32      2:8:2 172000        0      1     P100 not powering
gpu003         1      p100   draining@ 32      2:8:2 172000        0      1     P100 Kill task failed
gpu004         1      p100       mixed 32      2:8:2 172000        0      1     P100 none
gpu005         1      p100   draining@ 32      2:8:2 172000        0      1     P100 Kill task failed
gpu006         1      p100       mixed 32      2:8:2 172000        0      1     P100 none
gpu007         1      p100   draining@ 32      2:8:2 172000        0      1     P100 Kill task failed
```

## `squeue, scancel`
View the queue for sbatch jobs and cancel job given job ID

```sh
squeue [OPTIONS ...]
scancel [job_id]
```

`squeue` takes options to limit the display range, useful for large clusters

```sh
-p, --partition=<part_list>
# limit to specific partion or a comma separated list of partition names.

-q, --qos=<qos_list>
# limit to the qos(s) or a comma separated list of qos's.

-u, --user=<user_list>
# limit to the user or a comma separated list of users

-t, --states=<state_list>
# limit to the state of a comma separated list of states, case insensitive
```

Example
```sh
$> squeue -u user
  JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
8426702      t4v2    train     user  R    1:18:26      1 gpu063

$> scancel 8426702
$> squeue -u user
  JOBID PARTITION     NAME     USER ST       TIME  NODES NODELIST(REASON)
```

### `squeue` State Codes
A subset of the commonly seen state codes
```sh
BF BOOT_FAIL
# Job terminated due to launch failure, typically due to a hardware failure

CA CANCELLED
# Job was explicitly cancelled by the user or system administrator. 
# The job may or may not have been initiated.

CD COMPLETED
# Job has terminated all processes on all nodes with an exit code of zero.

F FAILED
# Job terminated with non-zero exit code or other failure condition.

OOM OUT_OF_MEMORY
# Job experienced out of memory error.

PD PENDING
# Job is awaiting resource allocation.

PR PREEMPTED
# Job terminated due to preemption.

ST STOPPED
# Job has an allocation, but execution has been stopped with SIGSTOP signal. 
# CPUS have been retained by this job.

S SUSPENDED
# Job has an allocation, but execution has been suspended and CPUs have been
# released for other jobs.

TO TIMEOUT
# Job terminated upon reaching its time limit.
```
