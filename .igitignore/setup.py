from setuptools import setup, find_packages

setup(
    name='ai_powered_chatbot_framework',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'tensorflow',
        'nltk',
        'spacy',
        'flask',
    ],
    entry_points={
        'console_scripts': [
            'chatbot=src.chatbot_engine:main',
        ],
    },
)
