from pylinac import FlatSym

file = "RI.Arck.1515-10FFFMV-0.dcm"

filImage = FlatSym(file)

filImage.analyze(flatness_method="iec", symmetry_method="pdq iec", vert_position=0.5, horiz_position=0.5)

print(filImage.results())  # print results
filImage.plot()  # matplotlib image
filImage.publish_pdf(filename="flatsym151510FFFMV02012018.pdf")  # create PDF and save to file