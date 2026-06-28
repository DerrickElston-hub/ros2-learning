import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger


class InspectionService(Node):

    def __init__(self):
        super().__init__('inspection_service')

        self.srv = self.create_service(
            Trigger,
            'start_inspection',
            self.start_callback
        )

        self.get_logger().info("Inspection Service Ready")


    def start_callback(self, request, response):

        self.get_logger().info("Inspection Started")

        response.success = True
        response.message = "Inspection Started Successfully"

        return response


def main(args=None):

    rclpy.init(args=args)

    node = InspectionService()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()