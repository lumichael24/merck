#NOTES

#OPTION 1: Using the Param File
3 Customizations 
	-Settings (determining how features are extracted)
	-Image Types (types of filters)
	-Feature Classes (which features we extract)

How do we set up a parameter file, the .yaml configuration file?

settings:
	label: 1 #default
	binWidth: 25 #default
	resampledPixelSpacing: [1, 1, 1] #increasing this spacing extracts more features from coarse textures (possibly deprecating)
  	padDistance: 10  # Extra padding for large sigma valued LoG filtered images

imageType: 
	original: {} #means no subfeatures of an original filter, for original, there are no subfeatures so we can omit the {}
	LoG: #Laplacian of Gaussian filter, emphasizes areas of gray level change
		sigma: [1.0, 2.0, 3.0, 4.0, 5.0] #refers to coarseness of texture
	Square: #subfeatures go below feature
	SquareRoot:
	Logarithm:
	Exponential:
	Gradient:
	LocalBinaryPattern2D:
	LocalBinaryPattern3D:

featureClass:
	shape: #volume, surface area, sphercity, compactness
	firstorder: #specifying nothing here means enabling all features, general values (entropy, 90 percentile, max, etc.)
		- '' #dash and feature name gives that specific feature
	glcm: #Gray Level Co-occurrence Matrix
	glrlm: #Gray Level Size Zone Matrix
	glszm: #Gray Level Run Length Matrix
	gldm: #Gray level Dependence Matrix
	ngtdm: #Neighboring Gray Tone Difference Matrix

#OPTION 2: Using the enableAllFeatures() function