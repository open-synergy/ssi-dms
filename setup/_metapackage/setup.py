import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-open-synergy-ssi-dms",
    description="Meta package for open-synergy-ssi-dms Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-ssi_dms',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
        'Framework :: Odoo :: 14.0',
    ]
)
