import shapefile
import matplotlib.pyplot as plt
from Instance import Instance

def read_file(filename):
    sf = shapefile.Reader(filename)
    return sf

def get_polygons(sf, zone_filter):
    r_shapes = []
    r_records = []
    shapes = sf.shapes()
    records = sf.records()
    for k in range(len(records)):
        shape = shapes[k]
        rec = records[k]
        if rec[5] in zone_filter:
            r_shapes.append(shape)
            r_records.append(rec)
    return r_shapes, r_records

def get_zones_ids(sf, zone_filter):
    ret = []
    records = sf.records()
    for k in range(len(records)):
        if records[k][5] in zone_filter:
            ret.append(k + 1)
    return ret

def visualize_zones():
    filename = '/Users/luanagiusto/PycharmProjects/TP Modelos/mygeodata/taxi_zones.shp'
    sf = read_file(filename)
    zone_filter = ['Manhattan']
    shapes, records = get_polygons(sf, zone_filter)
    zone_filter_ids = get_zones_ids(sf, zone_filter)

    for k in range(len(shapes)):
        shape = shapes[k]
        x = [i[0] for i in shape.points[:]]
        y = [i[1] for i in shape.points[:]]
        plt.plot(x, y, 'b')

def visualize_taxis(inst):
    for pnt in inst.taxis_longlat:
        plt.plot(pnt[0], pnt[1], '.g')

def visualize_paxs(inst):
    for pnt in inst.paxs_longlat:
        plt.plot(pnt[0], pnt[1], '.r')

def main():
    inst_types = ['small', 'medium', 'large', 'xl']
    n_inst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    for t in inst_types:
        for n in n_inst:
            filename = f'/Users/luanagiusto/PycharmProjects/TP Modelos/input/{t}_{n}.csv'
            inst = Instance(filename)

            plt.figure(figsize=(10, 6))  # Crear una nueva figura para cada instancia

            visualize_zones()
            visualize_paxs(inst)
            visualize_taxis(inst)

            plt.title(f'Visualización para {t}_{n}')
            plt.savefig(f'/Users/luanagiusto/PycharmProjects/TP Modelos/output/visualizations/{t}_{n}.png')  # Guardar la figura como un archivo PNG
            plt.close()  # Cerrar la figura para evitar sobrecargar la memoria

if __name__ == '__main__':
    main()
