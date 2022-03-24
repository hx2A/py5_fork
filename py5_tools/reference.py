# *****************************************************************************
#
#   Part of the py5 library
#   Copyright (C) 2020-2022 Jim Schmitz
#
#   This library is free software: you can redistribute it and/or modify it
#   under the terms of the GNU Lesser General Public License as published by
#   the Free Software Foundation, either version 2.1 of the License, or (at
#   your option) any later version.
#
#   This library is distributed in the hope that it will be useful, but
#   WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser
#   General Public License for more details.
#
#   You should have received a copy of the GNU Lesser General Public License
#   along with this library. If not, see <https://www.gnu.org/licenses/>.
#
# *****************************************************************************







PY5_DIR_STR = [
    '__version__',
    'acos',
    'ADD',
    'ALPHA',
    'alpha',
    'ALT',
    'AMBIENT',
    'ambient',
    'ambient_light',
    'apply_filter',
    'apply_matrix',
    'ARC',
    'arc',
    'ARGB',
    'ARGS_BGCOLOR',
    'ARGS_DISABLE_AWT',
    'ARGS_DISPLAY',
    'ARGS_EDITOR_LOCATION',
    'ARGS_EXTERNAL',
    'ARGS_FULL_SCREEN',
    'ARGS_HIDE_STOP',
    'ARGS_LOCATION',
    'ARGS_PRESENT',
    'ARGS_SKETCH_FOLDER',
    'ARGS_STOP_COLOR',
    'ARGS_UI_SCALE',
    'ARGS_WINDOW_COLOR',
    'ARROW',
    'asin',
    'atan',
    'atan2',
    'background',
    'BACKSPACE',
    'BASELINE',
    'begin_camera',
    'begin_closed_shape',
    'begin_contour',
    'begin_raw',
    'begin_record',
    'begin_shape',
    'BEVEL',
    'bezier',
    'bezier_detail',
    'bezier_point',
    'bezier_tangent',
    'BEZIER_VERTEX',
    'bezier_vertex',
    'bezier_vertices',
    'BLEND',
    'blend',
    'blend_mode',
    'blue',
    'BLUR',
    'BOTTOM',
    'BOX',
    'box',
    'BREAK',
    'brightness',
    'BURN',
    'camera',
    'ceil',
    'CENTER',
    'CHATTER',
    'CHORD',
    'circle',
    'CLAMP',
    'clip',
    'CLOSE',
    'CODED',
    'color',
    'color_mode',
    'COMPLAINT',
    'constrain',
    'CONTROL',
    'convert_image',
    'copy',
    'CORNER',
    'CORNERS',
    'cos',
    'create_font',
    'create_font_file',
    'create_graphics',
    'create_image',
    'create_image_from_numpy',
    'create_shape',
    'CROSS',
    'cursor',
    'curve',
    'curve_detail',
    'curve_point',
    'curve_tangent',
    'curve_tightness',
    'CURVE_VERTEX',
    'curve_vertex',
    'curve_vertices',
    'CUSTOM',
    'DARKEST',
    'day',
    'DEFAULT_HEIGHT',
    'DEFAULT_WIDTH',
    'DEG_TO_RAD',
    'degrees',
    'DELETE',
    'DIAMETER',
    'DIFFERENCE',
    'DILATE',
    'DIRECTIONAL',
    'directional_light',
    'DISABLE_ASYNC_SAVEFRAME',
    'DISABLE_BUFFER_READING',
    'DISABLE_DEPTH_MASK',
    'DISABLE_DEPTH_SORT',
    'DISABLE_DEPTH_TEST',
    'DISABLE_KEY_REPEAT',
    'DISABLE_NATIVE_FONTS',
    'DISABLE_OPENGL_ERRORS',
    'DISABLE_OPTIMIZED_STROKE',
    'DISABLE_STROKE_PERSPECTIVE',
    'DISABLE_STROKE_PURE',
    'DISABLE_TEXTURE_MIPMAPS',
    'display_density',
    'display_height',
    'display_width',
    'dist',
    'DODGE',
    'DOWN',
    'DXF',
    'ELLIPSE',
    'ellipse',
    'ellipse_mode',
    'emissive',
    'ENABLE_ASYNC_SAVEFRAME',
    'ENABLE_BUFFER_READING',
    'ENABLE_DEPTH_MASK',
    'ENABLE_DEPTH_SORT',
    'ENABLE_DEPTH_TEST',
    'ENABLE_KEY_REPEAT',
    'ENABLE_NATIVE_FONTS',
    'ENABLE_OPENGL_ERRORS',
    'ENABLE_OPTIMIZED_STROKE',
    'ENABLE_STROKE_PERSPECTIVE',
    'ENABLE_STROKE_PURE',
    'ENABLE_TEXTURE_MIPMAPS',
    'end_camera',
    'end_contour',
    'end_raw',
    'end_record',
    'end_shape',
    'ENTER',
    'EPSILON',
    'ERODE',
    'ESC',
    'EXCLUSION',
    'exit_sketch',
    'exp',
    'EXTERNAL_MOVE',
    'EXTERNAL_STOP',
    'fill',
    'finished',
    'floor',
    'focused',
    'frame_count',
    'frame_rate',
    'frustum',
    'full_screen',
    'FX2D',
    'get',
    'get_current_sketch',
    'get_frame_rate',
    'get_graphics',
    'get_matrix',
    'get_surface',
    'GIF',
    'GRAY',
    'green',
    'GROUP',
    'HALF_PI',
    'HAND',
    'HARD_LIGHT',
    'has_thread',
    'height',
    'HIDDEN',
    'hint',
    'HINT_COUNT',
    'hot_reload_draw',
    'hour',
    'HSB',
    'hue',
    'IMAGE',
    'image',
    'image_mode',
    'INVERT',
    'is_dead',
    'is_dead_from_error',
    'is_key_pressed',
    'is_mouse_pressed',
    'is_ready',
    'is_running',
    'JAVA2D',
    'java_platform',
    'java_version_name',
    'JClass',
    'JPEG',
    'key',
    'key_code',
    'LANDSCAPE',
    'launch_promise_thread',
    'launch_repeating_thread',
    'launch_thread',
    'LEFT',
    'lerp',
    'lerp_color',
    'light_falloff',
    'light_specular',
    'LIGHTEST',
    'lights',
    'LINE',
    'line',
    'LINE_LOOP',
    'LINE_STRIP',
    'LINES',
    'lines',
    'LINUX',
    'list_threads',
    'load_font',
    'load_image',
    'load_json',
    'load_np_pixels',
    'load_pixels',
    'load_shader',
    'load_shape',
    'log',
    'loop',
    'MACOS',
    'mag',
    'MAX_FLOAT',
    'MAX_INT',
    'millis',
    'MIN_FLOAT',
    'MIN_INT',
    'minute',
    'MITER',
    'MODEL',
    'model_x',
    'model_y',
    'model_z',
    'MODELVIEW',
    'month',
    'mouse_button',
    'mouse_x',
    'mouse_y',
    'MOVE',
    'MULTIPLY',
    'no_clip',
    'no_cursor',
    'no_fill',
    'no_lights',
    'no_loop',
    'no_smooth',
    'no_stroke',
    'no_tint',
    'noise',
    'noise_detail',
    'noise_seed',
    'norm',
    'NORMAL',
    'normal',
    'np_pixels',
    'NumpyImageArray',
    'OPAQUE',
    'OPEN',
    'OPENGL',
    'ortho',
    'ORTHOGRAPHIC',
    'os_noise',
    'os_noise_seed',
    'OTHER',
    'OVERLAY',
    'P2D',
    'P3D',
    'pargs',
    'parse_json',
    'PATH',
    'PDF',
    'PERSPECTIVE',
    'perspective',
    'PI',
    'PIE',
    'pixel_density',
    'pixel_height',
    'pixel_width',
    'pixels',
    'pmouse_x',
    'pmouse_y',
    'POINT',
    'point',
    'point_light',
    'POINTS',
    'points',
    'POLYGON',
    'pop',
    'pop_matrix',
    'pop_style',
    'PORTRAIT',
    'POSTERIZE',
    'print_camera',
    'print_line_profiler_stats',
    'print_matrix',
    'print_projection',
    'println',
    'PROBLEM',
    'profile_draw',
    'profile_functions',
    'PROJECT',
    'PROJECTION',
    'prune_tracebacks',
    'push',
    'push_matrix',
    'push_style',
    'Py5Font',
    'Py5Graphics',
    'Py5Image',
    'Py5Shader',
    'Py5Shape',
    'Py5Surface',
    'Py5Vector',
    'Py5Vector2D',
    'Py5Vector3D',
    'Py5Vector4D',
    'QUAD',
    'quad',
    'QUAD_BEZIER_VERTEX',
    'QUAD_STRIP',
    'QUADRATIC_VERTEX',
    'quadratic_vertex',
    'quadratic_vertices',
    'QUADS',
    'QUARTER_PI',
    'RAD_TO_DEG',
    'radians',
    'RADIUS',
    'random',
    'random_choice',
    'random_gaussian',
    'random_int',
    'random_seed',
    'RECT',
    'rect',
    'rect_mode',
    'red',
    'redraw',
    'register_exception_msg',
    'register_image_conversion',
    'remap',
    'render',
    'render_frame',
    'render_frame_sequence',
    'render_sequence',
    'REPEAT',
    'REPLACE',
    'request_image',
    'reset_matrix',
    'reset_py5',
    'reset_shader',
    'RETURN',
    'RGB',
    'RIGHT',
    'rotate',
    'rotate_x',
    'rotate_y',
    'rotate_z',
    'ROUND',
    'run_sketch',
    'saturation',
    'save',
    'save_frame',
    'save_json',
    'scale',
    'SCREEN',
    'screen_x',
    'screen_y',
    'screen_z',
    'second',
    'set_matrix',
    'set_np_pixels',
    'set_println_stream',
    'set_stackprinter_style',
    'shader',
    'SHAPE',
    'shape',
    'shape_mode',
    'shear_x',
    'shear_y',
    'SHIFT',
    'shininess',
    'sin',
    'size',
    'Sketch',
    'sketch_path',
    'smooth',
    'SOFT_LIGHT',
    'SPAN',
    'specular',
    'SPHERE',
    'sphere',
    'sphere_detail',
    'SPOT',
    'spot_light',
    'sq',
    'sqrt',
    'SQUARE',
    'square',
    'stop_all_threads',
    'stop_thread',
    'stroke',
    'stroke_cap',
    'stroke_join',
    'stroke_weight',
    'SUBTRACT',
    'SVG',
    'TAB',
    'tan',
    'TARGA',
    'TAU',
    'TEXT',
    'text',
    'text_align',
    'text_ascent',
    'text_descent',
    'text_font',
    'text_leading',
    'text_mode',
    'text_size',
    'text_width',
    'texture',
    'texture_mode',
    'texture_wrap',
    'THIRD_PI',
    'THRESHOLD',
    'TIFF',
    'tint',
    'TOP',
    'translate',
    'TRIANGLE',
    'triangle',
    'TRIANGLE_FAN',
    'TRIANGLE_STRIP',
    'TRIANGLES',
    'TWO_PI',
    'UP',
    'update_np_pixels',
    'update_pixels',
    'utils',
    'VERTEX',
    'vertex',
    'vertices',
    'WAIT',
    'WHITESPACE',
    'width',
    'window_move',
    'window_resizable',
    'window_resize',
    'window_title',
    'window_x',
    'window_y',
    'WINDOWS',
    'X',
    'Y',
    'year',
    'Z'
]

PY5_ALL_STR = [
    '__version__',
    'acos',
    'ADD',
    'ALPHA',
    'alpha',
    'ALT',
    'AMBIENT',
    'ambient',
    'ambient_light',
    'apply_filter',
    'apply_matrix',
    'ARC',
    'arc',
    'ARGB',
    'ARGS_BGCOLOR',
    'ARGS_DISABLE_AWT',
    'ARGS_DISPLAY',
    'ARGS_EDITOR_LOCATION',
    'ARGS_EXTERNAL',
    'ARGS_FULL_SCREEN',
    'ARGS_HIDE_STOP',
    'ARGS_LOCATION',
    'ARGS_PRESENT',
    'ARGS_SKETCH_FOLDER',
    'ARGS_STOP_COLOR',
    'ARGS_UI_SCALE',
    'ARGS_WINDOW_COLOR',
    'ARROW',
    'asin',
    'atan',
    'atan2',
    'background',
    'BACKSPACE',
    'BASELINE',
    'begin_camera',
    'begin_closed_shape',
    'begin_contour',
    'begin_raw',
    'begin_record',
    'begin_shape',
    'BEVEL',
    'bezier',
    'bezier_detail',
    'bezier_point',
    'bezier_tangent',
    'BEZIER_VERTEX',
    'bezier_vertex',
    'bezier_vertices',
    'BLEND',
    'blend',
    'blend_mode',
    'blue',
    'BLUR',
    'BOTTOM',
    'BOX',
    'box',
    'BREAK',
    'brightness',
    'BURN',
    'camera',
    'ceil',
    'CENTER',
    'CHATTER',
    'CHORD',
    'circle',
    'CLAMP',
    'clip',
    'CLOSE',
    'CODED',
    'color',
    'color_mode',
    'COMPLAINT',
    'constrain',
    'CONTROL',
    'convert_image',
    'copy',
    'CORNER',
    'CORNERS',
    'cos',
    'create_font',
    'create_font_file',
    'create_graphics',
    'create_image',
    'create_image_from_numpy',
    'create_shape',
    'CROSS',
    'cursor',
    'curve',
    'curve_detail',
    'curve_point',
    'curve_tangent',
    'curve_tightness',
    'CURVE_VERTEX',
    'curve_vertex',
    'curve_vertices',
    'CUSTOM',
    'DARKEST',
    'day',
    'DEFAULT_HEIGHT',
    'DEFAULT_WIDTH',
    'DEG_TO_RAD',
    'degrees',
    'DELETE',
    'DIAMETER',
    'DIFFERENCE',
    'DILATE',
    'DIRECTIONAL',
    'directional_light',
    'DISABLE_ASYNC_SAVEFRAME',
    'DISABLE_BUFFER_READING',
    'DISABLE_DEPTH_MASK',
    'DISABLE_DEPTH_SORT',
    'DISABLE_DEPTH_TEST',
    'DISABLE_KEY_REPEAT',
    'DISABLE_NATIVE_FONTS',
    'DISABLE_OPENGL_ERRORS',
    'DISABLE_OPTIMIZED_STROKE',
    'DISABLE_STROKE_PERSPECTIVE',
    'DISABLE_STROKE_PURE',
    'DISABLE_TEXTURE_MIPMAPS',
    'display_density',
    'dist',
    'DODGE',
    'DOWN',
    'DXF',
    'ELLIPSE',
    'ellipse',
    'ellipse_mode',
    'emissive',
    'ENABLE_ASYNC_SAVEFRAME',
    'ENABLE_BUFFER_READING',
    'ENABLE_DEPTH_MASK',
    'ENABLE_DEPTH_SORT',
    'ENABLE_DEPTH_TEST',
    'ENABLE_KEY_REPEAT',
    'ENABLE_NATIVE_FONTS',
    'ENABLE_OPENGL_ERRORS',
    'ENABLE_OPTIMIZED_STROKE',
    'ENABLE_STROKE_PERSPECTIVE',
    'ENABLE_STROKE_PURE',
    'ENABLE_TEXTURE_MIPMAPS',
    'end_camera',
    'end_contour',
    'end_raw',
    'end_record',
    'end_shape',
    'ENTER',
    'EPSILON',
    'ERODE',
    'ESC',
    'EXCLUSION',
    'exit_sketch',
    'exp',
    'EXTERNAL_MOVE',
    'EXTERNAL_STOP',
    'fill',
    'floor',
    'frame_rate',
    'frustum',
    'full_screen',
    'FX2D',
    'get',
    'get_current_sketch',
    'get_frame_rate',
    'get_graphics',
    'get_matrix',
    'get_surface',
    'GIF',
    'GRAY',
    'green',
    'GROUP',
    'HALF_PI',
    'HAND',
    'HARD_LIGHT',
    'has_thread',
    'HIDDEN',
    'hint',
    'HINT_COUNT',
    'hot_reload_draw',
    'hour',
    'HSB',
    'hue',
    'IMAGE',
    'image',
    'image_mode',
    'INVERT',
    'JAVA2D',
    'JClass',
    'JPEG',
    'LANDSCAPE',
    'launch_promise_thread',
    'launch_repeating_thread',
    'launch_thread',
    'LEFT',
    'lerp',
    'lerp_color',
    'light_falloff',
    'light_specular',
    'LIGHTEST',
    'lights',
    'LINE',
    'line',
    'LINE_LOOP',
    'LINE_STRIP',
    'LINES',
    'lines',
    'LINUX',
    'list_threads',
    'load_font',
    'load_image',
    'load_json',
    'load_np_pixels',
    'load_pixels',
    'load_shader',
    'load_shape',
    'log',
    'loop',
    'MACOS',
    'mag',
    'MAX_FLOAT',
    'MAX_INT',
    'millis',
    'MIN_FLOAT',
    'MIN_INT',
    'minute',
    'MITER',
    'MODEL',
    'model_x',
    'model_y',
    'model_z',
    'MODELVIEW',
    'month',
    'MOVE',
    'MULTIPLY',
    'no_clip',
    'no_cursor',
    'no_fill',
    'no_lights',
    'no_loop',
    'no_smooth',
    'no_stroke',
    'no_tint',
    'noise',
    'noise_detail',
    'noise_seed',
    'norm',
    'NORMAL',
    'normal',
    'NumpyImageArray',
    'OPAQUE',
    'OPEN',
    'OPENGL',
    'ortho',
    'ORTHOGRAPHIC',
    'os_noise',
    'os_noise_seed',
    'OTHER',
    'OVERLAY',
    'P2D',
    'P3D',
    'parse_json',
    'PATH',
    'PDF',
    'PERSPECTIVE',
    'perspective',
    'PI',
    'PIE',
    'pixel_density',
    'pixels',
    'POINT',
    'point',
    'point_light',
    'POINTS',
    'points',
    'POLYGON',
    'pop',
    'pop_matrix',
    'pop_style',
    'PORTRAIT',
    'POSTERIZE',
    'print_camera',
    'print_line_profiler_stats',
    'print_matrix',
    'print_projection',
    'println',
    'PROBLEM',
    'profile_draw',
    'profile_functions',
    'PROJECT',
    'PROJECTION',
    'prune_tracebacks',
    'push',
    'push_matrix',
    'push_style',
    'Py5Font',
    'Py5Graphics',
    'Py5Image',
    'Py5Shader',
    'Py5Shape',
    'Py5Surface',
    'Py5Vector',
    'Py5Vector2D',
    'Py5Vector3D',
    'Py5Vector4D',
    'QUAD',
    'quad',
    'QUAD_BEZIER_VERTEX',
    'QUAD_STRIP',
    'QUADRATIC_VERTEX',
    'quadratic_vertex',
    'quadratic_vertices',
    'QUADS',
    'QUARTER_PI',
    'RAD_TO_DEG',
    'radians',
    'RADIUS',
    'random',
    'random_choice',
    'random_gaussian',
    'random_int',
    'random_seed',
    'RECT',
    'rect',
    'rect_mode',
    'red',
    'redraw',
    'register_exception_msg',
    'register_image_conversion',
    'remap',
    'render',
    'render_frame',
    'render_frame_sequence',
    'render_sequence',
    'REPEAT',
    'REPLACE',
    'request_image',
    'reset_matrix',
    'reset_py5',
    'reset_shader',
    'RETURN',
    'RGB',
    'RIGHT',
    'rotate',
    'rotate_x',
    'rotate_y',
    'rotate_z',
    'ROUND',
    'run_sketch',
    'saturation',
    'save',
    'save_frame',
    'save_json',
    'scale',
    'SCREEN',
    'screen_x',
    'screen_y',
    'screen_z',
    'second',
    'set_matrix',
    'set_np_pixels',
    'set_println_stream',
    'set_stackprinter_style',
    'shader',
    'SHAPE',
    'shape',
    'shape_mode',
    'shear_x',
    'shear_y',
    'SHIFT',
    'shininess',
    'sin',
    'size',
    'Sketch',
    'sketch_path',
    'smooth',
    'SOFT_LIGHT',
    'SPAN',
    'specular',
    'SPHERE',
    'sphere',
    'sphere_detail',
    'SPOT',
    'spot_light',
    'sq',
    'sqrt',
    'SQUARE',
    'square',
    'stop_all_threads',
    'stop_thread',
    'stroke',
    'stroke_cap',
    'stroke_join',
    'stroke_weight',
    'SUBTRACT',
    'SVG',
    'TAB',
    'tan',
    'TARGA',
    'TAU',
    'TEXT',
    'text',
    'text_align',
    'text_ascent',
    'text_descent',
    'text_font',
    'text_leading',
    'text_mode',
    'text_size',
    'text_width',
    'texture',
    'texture_mode',
    'texture_wrap',
    'THIRD_PI',
    'THRESHOLD',
    'TIFF',
    'tint',
    'TOP',
    'translate',
    'TRIANGLE',
    'triangle',
    'TRIANGLE_FAN',
    'TRIANGLE_STRIP',
    'TRIANGLES',
    'TWO_PI',
    'UP',
    'update_np_pixels',
    'update_pixels',
    'utils',
    'VERTEX',
    'vertex',
    'vertices',
    'WAIT',
    'WHITESPACE',
    'window_move',
    'window_resizable',
    'window_resize',
    'window_title',
    'WINDOWS',
    'X',
    'Y',
    'year',
    'Z'
]

PY5_DYNAMIC_VARIABLES = [
    'display_height',
    'display_width',
    'finished',
    'focused',
    'frame_count',
    'height',
    'is_dead',
    'is_dead_from_error',
    'is_key_pressed',
    'is_mouse_pressed',
    'is_ready',
    'is_running',
    'java_platform',
    'java_version_name',
    'key',
    'key_code',
    'mouse_button',
    'mouse_x',
    'mouse_y',
    'np_pixels',
    'pargs',
    'pixel_height',
    'pixel_width',
    'pmouse_x',
    'pmouse_y',
    'width',
    'window_x',
    'window_y'
]

PY5_PYTHON_DYNAMIC_VARIABLES = [
    'pixels'
]
