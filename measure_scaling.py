import misure_manuali

DISTANCE_PRECISION = 3
SUM_PRECISION = 2
SCALING_PRECISION = 2
TOLERANCE = 0.01
SCALE_FACTOR = 50

def get_manual_measurements():
    return misure_manuali.misure_verticali

def build_object(measurements):
    distance_ratio = []
    total_points = []
    for i, obj in enumerate(measurements):
        label, numerator_ratio, points = obj
        total_points += points[:]

        temp_points = points[:]
        if i < len(measurements) - 1:
            next_obj = measurements[i + 1]
            _, _, end_points = next_obj
            temp_points += [end_points[0]]

        assert(len(temp_points) >= 2)
        distances = []
        for j in range(len(temp_points) - 1):
            distance = round(temp_points[j+1] - temp_points[j], DISTANCE_PRECISION)
            assert(distance >= 0)
            distances.append(distance)

        ratio = round(numerator_ratio / sum(distances), DISTANCE_PRECISION)
        distance_ratio.append((label, ratio, distances))

    total_distance = round(sum([sum(distances) for _, _, distances in distance_ratio]), SUM_PRECISION)
    start_end_difference = total_points[len(total_points) - 1] - total_points[0]
    assert(abs(total_distance - start_end_difference) < TOLERANCE)

    return distance_ratio, total_distance

def scale_distances(distance_ratio, scale_factor):
    scaled_distances = []
    verification_sum = 0
    max_distance_string_length = -1
    number_of_distances = 0
    for label, ratio, distances in distance_ratio:
        label_values = []
        number_of_distances += len(distances)
        for distance in distances:
            scaled = round(distance * ratio / scale_factor, SCALING_PRECISION)
            label_values.append((distance, scaled))
            verification_sum += scaled

            distance_string_length = len(f"{distance}{scaled}")
            max_distance_string_length = max(distance_string_length, max_distance_string_length)

        scaled_distances.append((label, label_values))
    
    return scaled_distances, round(verification_sum, SUM_PRECISION), (max_distance_string_length, number_of_distances)

def stringify_results(scaled_distances, total_distance, verification_sum, max_distance_string_length, number_of_distances):
    index = 0
    output = "Scaled Distances:\n"
    for label, distances in scaled_distances:
        output += f"{label}:\n"
        for distance, scaled in distances:
            index += 1
            distance_string_length = len(f"{distance}{scaled}")
            padding_distance_value_len = max_distance_string_length - distance_string_length
            padding_distance_value = " " * padding_distance_value_len
            padding_index_value_len = len(f"{number_of_distances}") - len(f"{index}")
            padding_index_value = " " * padding_index_value_len
            output += f"  {index}. {padding_index_value}{distance}{padding_distance_value} -> {scaled}\n"

    left_label = "manual measurements sum"
    right_label = "scaled sum"
    output += f"{left_label} -> {right_label}\n"
    padding = " " * (len(left_label) - len(f"{total_distance}"))
    output += f"{padding}{total_distance} -> {verification_sum}"
    return output

def main():
    measurements = get_manual_measurements()
    object_data, total_distance = build_object(measurements)
    scaled_data, verification_sum, (max_distance_length, instances_num) = scale_distances(object_data, SCALE_FACTOR)
    output = stringify_results(scaled_data, total_distance, verification_sum, max_distance_length, instances_num)
    print(output)

if __name__ == "__main__":
    main()
