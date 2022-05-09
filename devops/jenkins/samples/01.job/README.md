# Jenkins job

- A `job` is a task to be performed
- Show job: </job/job-name>

## Create job

- Create job: </view/all/newJob>
  - Give it any name
  - Freestyle project

## Configure project

- Configure job: </job/job-name/configure>

### Execute shell

- `Build->Execute shell`: run a shell script

```shell
NAME=Henrique # temporary environment variable
echo "Hello World"
echo "Current date is $(date)"
echo "Hello, $NAME. The current date and time is $(date)"
echo "Hello, $NAME. The current date and time is $(date)" > /tmp/info # Save the log in a file
```

### Parameterized job

- Check `This job is parametrized` to define envs
  - string, choice (list), boolean, etc

```shell
echo "Hello, $NAME. The current date and time is $(date)." > /tmp/hello.txt # The $NAME will be defined in jenkins
```

### Script job

- Define shell script to be executed

```shell
/tmp/script.sh $FIRST_NAME $LAST_NAME $SHOW # run script with parameters
```

```shell
# copy the script into the container
docker container cp "./script.sh" "jenkins:/tmp/script.sh"
```

## Build

- Build job: </job/job-name/build>
- If an execution fails it will show as a red ball
