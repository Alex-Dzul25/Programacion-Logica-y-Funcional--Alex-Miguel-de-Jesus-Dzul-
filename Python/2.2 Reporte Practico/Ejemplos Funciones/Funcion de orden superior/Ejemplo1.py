def seleccionar_formato(formato):
    def pdf():
        return "Exportando en PDF"

    def csv():
        return "Exportando en CSV"

    return pdf if formato == "pdf" else csv

exportacion = seleccionar_formato("csv")
print(exportacion())  
