python3 setup.py sdist bdist_wheel
twine upload dist/*
rm -r mpx_api.egg-info
rm -r dist/
rm -r build/
