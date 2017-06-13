#!/bin/sh
#Before running this script, you must initialize git
#and create the CNAME file inside dirhtml
docdir=/PATH_TO_PROJECT/doc/ &&
mv ${docdir}_build/dirhtml/.git ${docdir}_build/.git &&
mv ${docdir}_build/dirhtml/CNAME ${docdir}_build/CNAME &&
rm -rfv ${docdir}_build/dirhtml/ &&
rm -rfv ${docdir}_build/doctrees/ &&
mkdir ${docdir}_build/dirhtml/ &&
mv ${docdir}_build/.git ${docdir}_build/dirhtml/.git &&
mv ${docdir}_build/CNAME ${docdir}_build/dirhtml/CNAME &&
cd ${docdir} &&
make dirhtml &&
cd ${docdir}_build/dirhtml &&
touch .nojekyll &&
git add -A &&
git commit -m "update" &&
git push
