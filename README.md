# low-level-design
Low Level Design problems

## Run Java Projects (Auto Compile)

Use the repo-level runner. It compiles first, then runs:

```bash
./run-java.sh JAVA/notificationsystem
```

Optional explicit main class:

```bash
./run-java.sh JAVA/notificationsystem notificationsystem.Main
```

## Clean Java Artifacts

Delete compiled artifacts across the full repo (`.class`, `out/`, `build/`):

```bash
./clean-java.sh
```
