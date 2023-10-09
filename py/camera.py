import numpy as np
import cv2
import tensorflow as tf


cap = cv2.VideoCapture(0)

while True:
    # Read frame from camera
    ret, image_np = cap.read()

    # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
    image_np_expanded = np.expand_dims(image_np, axis=3)

    # Convert image to grayscale

    def detect_fn(input_tensor):

        input_tensor = tf.convert_to_tensor(np.expand_dims(image_np, 0), dtype=tf.float32)
        detections, predictions_dict, shapes = detect_fn(input_tensor)

    label_id_offset = 1
    image_np_with_detections = image_np.copy()

    def viz_utils_visualize_boxes_and_labels_on_image_array(
    image_np_with_detections,
    detection_boxes,
    detection_classes,
    detection_scores,
    category_index,
    use_normalized_coordinates=True,
    max_boxes_to_draw=200,
    min_score_thresh=0.30,
    agnostic_mode=False):
    # Function implementation goes here
     pass

    # Call the function
    [viz_utils_visualize_boxes_and_labels_on_image_array]( 
        image_np_with_detections,
        detections['detection_boxes'][0].numpy(),
        detections['detection_classes'][0].numpy() + label_id_offset,
        detections['detection_scores'][0].numpy(),
        category_index,
        use_normalized_coordinates=True,
        max_boxes_to_draw=200,
        min_score_thresh=0.30,
        agnostic_mode=False
        )

    # Display output
    cv2.imshow('object detection', cv2.resize(image_np_with_detections, (800, 600)))
    cv2.resize(image_np_with_detections, (1200,900))

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()