import rclpy
from rclpy.node import Node


class InspectionParameterNode(Node):

    def __init__(self):
        super().__init__('inspection_parameter_node')

        self.declare_parameter('confidence_threshold', 0.90)

        threshold = self.get_parameter(
            'confidence_threshold'
        ).value

        self.get_logger().info(
            f'Confidence Threshold: {threshold}'
        )


def main(args=None):

    rclpy.init(args=args)

    node = InspectionParameterNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()