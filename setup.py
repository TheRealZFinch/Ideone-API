import setuptools

setuptools.setup(
    name="ideoneapi", 
    url="https://github.com/TheRealZFinch/Ideone-API",                    
    version="0.0.1",                        
    author="TheRealZFinch",
    license="MIT",        
    description="Ideone API",
    long_description="This Python package allows getting information about projects on Ideone",      
    long_description_content_type="text",
    packages=setuptools.find_packages(),    
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],                                      
    python_requires='>=3.8',                 
    install_requires=["bs4","beautifulsoup4","soupsieve","requests"]                    
)
