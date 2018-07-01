import sap

materials = sap.Sap().get_material_list()
for m in materials:
    print(m.get_text())