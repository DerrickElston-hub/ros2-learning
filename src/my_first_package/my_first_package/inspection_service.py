import rclpy
from rclpy.node import Node

from my_robot_interfaces.srv import Inspection


class InspectionService(Node):

    def __init__(self):
        super().__init__('inspection_service')

        self.srv = self.create_service(
            Inspection,
            'inspect_part',
            self.start_callback
        )

        self.get_logger().info("Custom Inspection Service Ready")

    def start_callback(self, request, response):

        self.get_logger().info(
            f"Inspecting Part ID: {request.part_id}"
        )

        response.passed = True
        response.confidence = 0.96
        response.message = "Inspection Passed"

        return response


def main(args=None):

    rclpy.init(args=args)

    node = InspectionService()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()