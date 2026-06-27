import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class InspectionCameraNode(Node):

    def __init__(self):
        super().__init__('inspection_camera_node')

        self.publisher_ = self.create_publisher(
            String,
            '/inspection_data',
            10
        )

        timer_period = 1.0
        self.timer = self.create_timer(
            timer_period,
            self.publish_inspection_data
        )

        self.part_id = 100

    def publish_inspection_data(self):
        msg = String()

        msg.data = (
            f"Part ID: {self.part_id} | "
            f"Confidence: 0.94 | "
            f"Status: PASS"
        )

        self.publisher_.publish(msg)

        self.get_logger().info(f"Publishing: {msg.data}")

        self.part_id += 1


def main(args=None):
    rclpy.init(args=args)

    node = InspectionCameraNode()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()