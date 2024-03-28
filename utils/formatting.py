def yolo_to_coco(labels):
    coco_labels = []
    for bbox in labels:
        x, y, w, h = bbox
        x_min = x - w / 2
        y_min = y - h / 2
        coco_labels.append([x_min, y_min, w, h])
    return coco_labels

def coco_to_yolo(labels):
    yolo_labels = []
    for bbox in labels:
        x_min, y_min, w, h = bbox
        x = x_min + w / 2
        y = y_min + h / 2
        yolo_labels.append([x, y, w, h])
    return yolo_labels

def yolo_to_pascalVoc(labels):
    pascalVoc_labels = []
    for bbox in labels:
        x_center, y_center, w, h = bbox
        x_min = x_center - w / 2
        y_min = y_center - h / 2
        x_max = x_center + w / 2
        y_max = y_center + h / 2
        pascalVoc_labels.append([x_min, y_min, x_max, y_max])
    return pascalVoc_labels

def pascalVoc_to_yolo(labels):
    yolo_labels = []
    for bbox in labels:
        x_min, y_min, x_max, y_max = bbox
        x_center = (x_min + x_max) / 2
        y_center = (y_min + y_max) / 2
        w = x_max - x_min
        h = y_max - y_min
        yolo_labels.append([x_center, y_center, w, h])
    return yolo_labels

def unnormalize_bbox(bboxes, image_shape):
    unnormalized_bboxes = []
    for bbox in bboxes:
        x, y, w, h = bbox
        x, y, w, h = x * image_shape[1], y * image_shape[0], w * image_shape[1], h * image_shape[0]
        unnormalized_bboxes.append([x, y, w, h])
    return unnormalized_bboxes
