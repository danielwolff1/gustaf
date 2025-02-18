import numpy as np

import gustaf as gus

if __name__ == "__main__":
    f = gus.Faces()
    f.vertices = [
        [1.16670818, 0.116044],
        [1.16670818, 0.32152345],
        [1.15581154, 0.36407223],
        [1.13713159, 0.38949772],
        [1.11274388, 0.40143213],
        [1.08368618, 0.40454545],
        [1.03854296, 0.39676214],
        [0.97731424, 0.37393109],
        [0.92334994, 0.33709008],
        [0.9, 0.28831465],
        [0.91867995, 0.24161478],
        [0.96330428, 0.2198215],
        [0.96330428, -0.3322748],
        [0.93528435, -0.340577],
        [0.91712329, -0.36081362],
        [0.90778331, -0.38520133],
        [0.90518888, -0.4069946],
        [0.90518888, -0.41218348],
        [0.92334994, -0.45213782],
        [0.96019095, -0.47496887],
        [1.0079286, -0.48482773],
        [1.05877958, -0.48690328],
        [1.07953508, -0.48690328],
        [1.13557493, -0.48430884],
        [1.18331258, -0.4734122],
        [1.21652138, -0.44954338],
        [1.22897468, -0.40803238],
        [1.21704027, -0.36859693],
        [1.18123703, -0.33538813],
        [1.16826484, -0.31359485],
        [1.1656704, -0.27519718],
        [1.16618929, -0.25184724],
        [1.16670818, -0.2326484],
        [1.16618929, -0.20877958],
        [1.1656704, -0.1828352],
        [1.16826484, -0.13509755],
        [1.17916148, -0.091511],
        [1.20406808, -0.05985886],
        [1.2486924, -0.04792445],
        [1.29227895, -0.05933998],
        [1.3234122, -0.09099211],
        [1.34209215, -0.13821088],
        [1.3483188, -0.19632628],
        [1.3483188, -0.2077418],
        [1.33534662, -0.31307597],
        [1.3109589, -0.42152345],
        [1.30992113, -0.43293898],
        [1.31718555, -0.46044002],
        [1.33638439, -0.48327107],
        [1.36336654, -0.49883769],
        [1.39294313, -0.50454545],
        [1.44794521, -0.48897883],
        [1.49153176, -0.44227895],
        [1.49153176, -0.44124118],
        [1.56002491, -0.18387298],
        [1.54134496, -0.05466999],
        [1.48738066, 0.04806974],
        [1.40072644, 0.11552511],
        [1.28397675, 0.13991283],
        [1.60983811, -0.3322748],
        [1.57870486, -0.34991698],
        [1.56106268, -0.37119137],
        [1.55327937, -0.39298464],
        [1.55172271, -0.4111457],
        [1.56832711, -0.45577003],
        [1.61087588, -0.47860108],
        [1.66899128, -0.48690328],
        [1.73125778, -0.48794105],
        [1.78003321, -0.48223329],
        [1.8220631, -0.46614778],
        [1.8511208, -0.44124118],
        [1.86201743, -0.40907015],
        [1.81427978, -0.3364259],
        [1.81427978, 0.0454753],
        [1.79092985, 0.1077418],
        [1.73748443, 0.12642175],
        [1.66276463, 0.11500623],
        [1.60361146, 0.08594853],
        [1.56417601, 0.04755085],
        [1.54964716, 0.00915318],
        [1.56002491, -0.02716895],
        [1.60361146, -0.05518888],
        [1.60931922, -0.11382316],
        [1.61087588, -0.17141968],
        [1.60983811, -0.23161063],
        [1.60880033, -0.29180158],
        [1.60931922, -0.31203819],
        [1.71154006, 0.3900166],
        [1.69908676, 0.3900166],
        [1.65653798, 0.38067663],
        [1.62177252, 0.35525114],
        [1.59790369, 0.31841013],
        [1.58908261, 0.27586135],
        [1.59894147, 0.2322748],
        [1.62488584, 0.19595268],
        [1.66172686, 0.17156496],
        [1.70531341, 0.16274388],
        [1.7514944, 0.17208385],
        [1.78781652, 0.19699045],
        [1.81168535, 0.23331258],
        [1.82050643, 0.27689913],
        [1.81168535, 0.31892902],
        [1.78781652, 0.35525114],
        [1.75305106, 0.38067663],
    ]

    f.faces = [
        [16, 17, 18],
        [15, 18, 19],
        [16, 18, 15],
        [12, 13, 14],
        [14, 15, 12],
        [15, 19, 12],
        [12, 20, 21],
        [12, 21, 22],
        [12, 29, 30],
        [22, 29, 12],
        [30, 31, 12],
        [22, 23, 28],
        [20, 12, 19],
        [32, 12, 31],
        [8, 9, 10],
        [8, 10, 11],
        [8, 11, 7],
        [7, 11, 6],
        [6, 1, 5],
        [6, 11, 1],
        [34, 35, 12],
        [36, 0, 11],
        [12, 35, 11],
        [1, 11, 0],
        [3, 4, 2],
        [2, 4, 5],
        [1, 2, 5],
        [12, 33, 34],
        [12, 32, 33],
        [24, 25, 26],
        [29, 22, 28],
        [27, 28, 24],
        [24, 26, 27],
        [28, 23, 24],
        [45, 48, 49],
        [45, 49, 50],
        [45, 50, 51],
        [47, 48, 45],
        [47, 45, 46],
        [45, 51, 53],
        [51, 52, 53],
        [44, 45, 53],
        [35, 36, 11],
        [38, 58, 0],
        [57, 58, 39],
        [39, 58, 38],
        [0, 37, 38],
        [39, 40, 56],
        [37, 0, 36],
        [43, 44, 54],
        [42, 54, 41],
        [54, 42, 43],
        [44, 53, 54],
        [40, 41, 55],
        [39, 56, 57],
        [56, 40, 55],
        [41, 54, 55],
        [62, 63, 65],
        [62, 60, 61],
        [65, 60, 62],
        [65, 63, 64],
        [73, 82, 83],
        [72, 85, 86],
        [72, 84, 85],
        [72, 83, 84],
        [86, 59, 72],
        [60, 65, 59],
        [79, 80, 78],
        [92, 93, 91],
        [78, 80, 81],
        [81, 76, 77],
        [94, 90, 91],
        [90, 94, 88],
        [94, 91, 93],
        [73, 81, 82],
        [77, 78, 81],
        [59, 65, 66],
        [72, 73, 83],
        [75, 76, 73],
        [67, 72, 59],
        [68, 72, 67],
        [69, 70, 71],
        [69, 71, 72],
        [75, 73, 74],
        [76, 81, 73],
        [69, 72, 68],
        [87, 95, 96],
        [102, 87, 96],
        [88, 89, 90],
        [88, 95, 87],
        [96, 97, 102],
        [94, 95, 88],
        [101, 98, 99],
        [101, 99, 100],
        [102, 103, 87],
        [102, 98, 101],
        [102, 97, 98],
        [66, 67, 59],
    ]

    f.vertex_data["arange"] = np.arange(len(f.vertices))
    f.show_options["data_name"] = "arange"
    f_2d = f.copy()
    f.show_options["scalarbar3d"] = {
        "title": "scalarbar title",
        "nlabels": 2,
    }
    f_2d.show_options["scalarbar"] = {
        "nlabels": 12,
    }
    gus.show.show([f, "3D scalarbar"], [f_2d, "2D scalarbar"])
