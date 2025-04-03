# SPDX-FileCopyrightText: 2023-2025 Espressif Systems (Shanghai) CO LTD
# SPDX-License-Identifier: CC0-1.0

import pytest
import cv2
from pytest_embedded import Dut


def bsp_capture_image(image_path):
    # Return video from the first webcam on your computer.
    cap = cv2.VideoCapture(0)
    # Set 4K resolution (3840x2160)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 3840)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2160)
    # reads frames from a camera
    # ret checks return at each frame
    ret, frame = cap.read()
    if ret:
        # TODO: Change size image
        # TODO: Crop image

        # Save image
        cv2.imwrite(image_path, frame)
        print(f"Image saved {image_path}")
    else:
        print("Cannot save image.")

    # Close the window / Release webcam
    cap.release()


def bsp_test_image(board, example, expectation):
    image_file = f"snapshot_{example}_{board}.jpg"
    bsp_capture_image(image_file)


@pytest.mark.esp_box_3
@pytest.mark.esp32_p4_function_ev_board
@pytest.mark.esp32_c3_lcdkit
@pytest.mark.esp32_s3_eye
@pytest.mark.esp32_s3_lcd_ev_board
@pytest.mark.esp32_s3_lcd_ev_board_2
@pytest.mark.esp32_s3_usb_otg
@pytest.mark.esp_wrover_kit
@pytest.mark.esp32_s3_korvo_2
@pytest.mark.m5dial
@pytest.mark.m5stack_core
@pytest.mark.m5stack_core_2
@pytest.mark.m5stack_core_s3
@pytest.mark.m5stack_core_s3_se
@pytest.mark.m5_atom_s3
def test_display_example(dut: Dut, request) -> None:
    board = request.node.callspec.id
    dut.expect_exact('example: Display LVGL animation')
    dut.expect_exact('main_task: Returned from app_main()')
    bsp_test_image(board, "display", "")
