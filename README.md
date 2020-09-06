# PA Vote By Mail

More than [550,000 Americans had their mail-in ballots rejected](https://www.npr.org/2020/08/22/904693468/more-than-550-000-primary-absentee-ballots-rejected-in-2020-far-outpacing-2016) in the 2020 primaries. Over half a million people who tried to vote ended up having their voices ignored because there was a problem with their ballot.

**37,119** of those rejected ballots were from Pennsylvania.

The goal of this site is to teach people in PA how to vote successfully by mail so that their vote is actually counted.

## Developing pavotebymail

### Install dependencies

```bash
$ brew install postgresql openssl
$ export LDFLAGS=$(pg_config --ld_flags)
$ pipenv install 
```

### Start docker-compose for databases

Before you can import data you'll need to be running the databases

```bash
$ docker-compose -f docker/dev-compose.yml up
```

### Run tests

```bash
pipenv run pytest
```

### Import database data so you can explore it on your local machine

```bash
$ pipenv run pavotebymail data-import --import-config phildelphia --postgres-password example /path/to/data_to_import.py
```

### Populate google firestore database

```bash
# tbd
```

### Run the worker and fake send postcards

```bash
# tbd
```
