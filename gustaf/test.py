import gustaf as gus
import numpy as np

bez = gus.Bezier(
    degrees=[1],
    control_points=[
        [1, 1],
        [2, 2]
    ]
).rationalbezier

bez.create.extrude(axis=[-1, 1]).show()

bez.create.revolve(axis=[0, 0], angle=np.pi*.5).show()

# bez1 = gus.Bezier(
#    degrees=[1,1],
#    control_points=
#      [
#          [0.5, 0. , 0.],
#          [1. , 0.5, 0.],
#          [0. , 0.5, 0.],
#          [.5 , 1. , 0.]
#      ]
# ).nurbs
#bez2 = bez1.create.extrude(axis=[0,0,1])
# bez2.show()
#
# bez1 = gus.RationalBezier(
#    degrees=[1,1],
#    control_points=
#      [
#          [0.5, 0.1, 0.],
#          [1. , 0.6, 0.],
#          [0. , 0.6, 0.],
#          [.5 , 1.1, 0.]
#      ],
#    weights=[1,1,1,1]
# )
# bez3 = bez1.create.revolve(
#    axis=[1,0,0],
#    angle=np.pi * 0.9
#    )
#
# bez3.show()
