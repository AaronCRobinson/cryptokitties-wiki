# cryptokitties-wiki

Includes dockerfile, configuration files, and wiki-data for cryptokittieswiki.com. 

Forked from [camandel/docker-django-wiki](https://github.com/camandel/docker-django-wiki)

### Installation & Usage
To download
```sh
$ git clone https://github.com/AaronCRobinson/cryptokitties-wiki.git ~/src
$ docker build .
$ docker run -d -p 80:8000 -v ~/src/testproject/testproject/db:/db:z -v ~/src/testproject/testproject/templates:/templates:z -v ~/src/testproject/testproject/settings:/settings:z -v ~/src/testproject/testproject/media:/wikimedia:z --name=cryptokitties-wiki3 fcc825d3e8ac
```

### Restarting
```sh
docker restart django-wiki
```

### Backup
To backup the sqlite db copy it to a local directory or use a persistent volume:
```sh
$ echo '.dump' | sqlite3 ~/src/testproject/testproject/db/db.sqlite3 > ~/wiki.dump
```
To restore:
```sh
$ sqlite3 /mydata/db/db.sqlite3 < /mydata/backup/wiki.dump
```
