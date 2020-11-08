#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace

if [ ! -f /tmp/google-10000-english.txt ]; then
  wget -O /tmp/google-10000-english.txt 'https://github.com/first20hours/google-10000-english/raw/master/google-10000-english.txt'
fi

if [ ! -f /tmp/obscene.list ]; then
  wget -O /tmp/obscene.list 'https://github.com/LDNOOBW/List-of-Dirty-Naughty-Obscene-and-Otherwise-Bad-Words/raw/master/en'
fi

echo > /tmp/dictionaries.list
if [ -f /usr/share/dict/british-english ]; then
  cat /usr/share/dict/british-english | awk '$0 ~ /^[a-z]{4,10}$/' > /tmp/dictionaries.list
fi
if [ -f /usr/share/dict/american-english ]; then
  cat /usr/share/dict/american-english | awk '$0 ~ /^[a-z]{4,10}$/' >> /tmp/dictionaries.list
fi

cat /tmp/google-10000-english.txt /tmp/obscene.list \
    | grep -v -P '[*+]' \
    | sed 's/"//g' | sed "s/'//g" | sed -e 's/^\s+//g' -e 's/\s+$//g' \
    | sed 's/[“”]//g' | sed 's/_/ /g' \
    | awk '{print tolower($0)}' | awk 'length($0) > 1' \
    | grep -v -P '^(un|re|in)' \
    | grep -v -P '(ing|er|ers|ness|ed)$' \
    | sort -u \
    | shuf > words.short.list

cat /tmp/google-10000-english.txt /tmp/obscene.list /tmp/dictionaries.list \
    | grep -v -P '[*+]' \
    | sed 's/"//g' | sed "s/'//g" | sed -e 's/^\s+//g' -e 's/\s+$//g' \
    | sed 's/[“”]//g' | sed 's/_/ /g' \
    | awk '{print tolower($0)}' | awk 'length($0) > 1' \
    | grep -v -P '^(un|re|in)' \
    | grep -v -P '(ing|er|ers|ness|ed)$' \
    | sort -u \
    | shuf > words.long.list
