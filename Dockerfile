FROM python

# Install dependencies.
RUN apt-get update && apt-get install -y \
  openssl \
  postgresql

# Set env vars for postgres.
ENV LDFLAGS $(pg_config --ldflags)

# Install pipenv.
RUN pip install pipenv

# Install our project dependencies.
# Docs: https://pipenv-fork.readthedocs.io/en/latest/basics.html#pipenv-install
# --dev — Install both develop and default packages from Pipfile.
# --system — Use the system pip command rather than the one from your
#            virtualenv.
# --deploy — Make sure the packages are properly locked in Pipfile.lock, and
#            abort if the lock file is out-of-date.
# --ignore-pipfile — Ignore the Pipfile and install from the Pipfile.lock.
# --skip-lock — Ignore the Pipfile.lock and install from the Pipfile. In
#               addition, do not write out a Pipfile.lock reflecting changes to
#               the Pipfile.
COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock
RUN pipenv install --system --dev

# Setup docker image to run as an executable.
ENTRYPOINT [ "pipenv", "run" ]
