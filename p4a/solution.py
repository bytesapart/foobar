import math


def solution(dimensions, your_position, trainer_position, distance):
    # Your code here
    # This program runs on 2 major principles. One is that of reflection of the co-ordinates
    # this way you can compute the "bounce" and the other is determining the angle of
    # fire. With these two, one can then loojup if we are hitting our reflected self or not
    # if so, we can discard the shots at those angles

    # ===== Step 1: Setup the positive quadrant, aka, first quadrant =====
    initial_state = setup_first_quadrant_with_reflections(dimensions, your_position, trainer_position, distance)

    # ===== Step 2: Replicate reflected Quadrant to other quadrants to mimic shooting in left, left-down and down direction
    second_quadrant, third_quadrant, fourth_quadrant = setup_all_mirrored_quadrants(initial_state, your_position, distance)
    final_state = initial_state + second_quadrant + third_quadrant + fourth_quadrant

    # ===== Filter the list according to angles =====
    final_filtered_states = get_valid_hits(final_state, your_position, distance)
    return sum([1 for key in final_filtered_states if final_filtered_states[key][0][2] == 1])


def get_valid_hits(final_state, your_position, max_distance):
    target = {}
    for i in range(len(final_state)):
        distance = distance_formula(final_state[i][0], your_position[0], final_state[i][1], your_position[1])
        angle = math.atan2(final_state[i][1] - your_position[1], final_state[i][0] - your_position[0])
        cond_one = max_distance >= distance > 0
        cond_two = angle not in target
        cond_three = angle in target and distance < target[angle][1]
        if cond_one and (cond_two or cond_three):
            target[angle] = [final_state[i], distance]

    return target


def setup_all_mirrored_quadrants(initial_state, your_position, max_distance):
    second_quadrant, temp_second_quadrant = [], []
    third_quadrant, temp_third_quadrant = [], []
    fourth_quadrant, temp_fourth_quadrant = [], []

    # Unit vectors
    second_quadrant_unit_vector = [-1, 1]
    third_quadrant_unit_vector = [-1, -1]
    fourth_quadrant_unit_vector = [1, -1]

    for position in initial_state:
        temp_second_quadrant.append(
            [position[0] * second_quadrant_unit_vector[0], position[1] * second_quadrant_unit_vector[1], position[2]])
        temp_third_quadrant.append(
            [position[0] * third_quadrant_unit_vector[0], position[1] * third_quadrant_unit_vector[1], position[2]])
        temp_fourth_quadrant.append(
            [position[0] * fourth_quadrant_unit_vector[0], position[1] * fourth_quadrant_unit_vector[1], position[2]])

    for position in temp_second_quadrant:
        distance = distance_formula(position[0], your_position[0], position[1], your_position[1])
        if distance <= max_distance:
            second_quadrant.append(position)

    for position in temp_third_quadrant:
        distance = distance_formula(position[0], your_position[0], position[1], your_position[1])
        if distance <= max_distance:
            third_quadrant.append(position)

    for position in temp_fourth_quadrant:
        distance = distance_formula(position[0], your_position[0], position[1], your_position[1])
        if distance <= max_distance:
            fourth_quadrant.append(position)

    return second_quadrant, third_quadrant, fourth_quadrant


def setup_first_quadrant_with_reflections(dimensions, your_position, trainer_position, distance):
    # Calculate the max distance of the ray from me, account for my position
    max_ray_x = distance + your_position[0] + 1
    max_ray_y = distance + your_position[1] + 1

    # Get number of reflected rooms to create
    reflections_along_x = int(math.ceil(max_ray_x / dimensions[0]))
    reflections_along_y = int(math.ceil(max_ray_y / dimensions[1]))

    my_position_in_x_reflections = []
    my_position_in_y_reflections = []
    trainer_position_in_x_reflections = []
    trainer_position_in_y_reflections = []

    for x in xrange(0, reflections_along_x + 1):
        temp_my_y_list = []
        temp_trainer_y_list = []
        reflected_x = dimensions[0] * x

        if not my_position_in_x_reflections:
            reflected_my_position_x = your_position[0]
        else:
            reflected_my_position_x = (reflected_x - my_position_in_x_reflections[-1][0]) + reflected_x
        # We set a flag 0 to indicate this vector belongs to me, and 1 to indicate if it belongs to trainer
        my_position_in_x_reflections.append([reflected_my_position_x, your_position[1], 0])

        if not trainer_position_in_x_reflections:
            reflected_trainer_position_x = trainer_position[0]
        else:
            reflected_trainer_position_x = (reflected_x - trainer_position_in_x_reflections[-1][0]) + reflected_x
        # Set 1 flag for trainer
        trainer_position_in_x_reflections.append([reflected_trainer_position_x, trainer_position[1], 1])

        for y in xrange(1, reflections_along_y + 1):
            reflected_y = dimensions[1] * y

            if not temp_my_y_list:
                reflected_my_position_y = (reflected_y - your_position[1]) + reflected_y
                temp_my_y_list.append(reflected_my_position_y)
            else:
                reflected_my_position_y = (reflected_y - temp_my_y_list[-1]) + reflected_y
                temp_my_y_list.append(reflected_my_position_y)
            my_position_in_y_reflections.append([reflected_my_position_x, reflected_my_position_y, 0])

            if not temp_trainer_y_list:
                reflected_trainer_position_y = (reflected_y - trainer_position[1]) + reflected_y
                temp_trainer_y_list.append(reflected_trainer_position_y)
            else:
                reflected_trainer_position_y = (reflected_y - temp_trainer_y_list[-1]) + reflected_y
                temp_trainer_y_list.append(reflected_trainer_position_y)
            trainer_position_in_y_reflections.append([reflected_trainer_position_x, reflected_trainer_position_y, 1])

    return my_position_in_x_reflections + my_position_in_y_reflections + trainer_position_in_x_reflections + trainer_position_in_y_reflections


def distance_formula(x1, x2, y1, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


dimensions = [3, 2]
your_position = [1, 1]
trainer_position = [2, 1]
distance = 4
solution(dimensions, your_position, trainer_position, distance)
