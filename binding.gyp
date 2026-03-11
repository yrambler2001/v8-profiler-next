{
  'includes': [
    'config.gypi'
  ],

  'variables': {
    'action_after_build': 'false'
  },

  'targets': [
    {
      'target_name': 'profiler',
      'win_delay_load_hook': 'false',
      'sources': [
        'src/cpu_profiler/cpu_profiler.cc',
        'src/cpu_profiler/cpu_profile.cc',
        'src/cpu_profiler/cpu_profile_node.cc',
        'src/heap_profiler/sampling_heap_profiler.cc',
        'src/heapsnapshot/heap_profiler.cc',
        'src/heapsnapshot/heap_snapshot.cc',
        'src/heapsnapshot/heap_output_stream.cc',
        'src/heapsnapshot/heap_graph_node.cc',
        'src/heapsnapshot/heap_graph_edge.cc',
        'src/profiler.cc',
        'src/environment_data.cc'
      ],
      'include_dirs' : [
        'src',
        '<!(node -e "require(\'nan\')")'
      ],
      'conditions':[
        ['OS == "linux"', {
          'cflags_cc': [
            '-O2',
            '-std=c++20',
            '-Wno-sign-compare',
            '-Wno-cast-function-type',
          ],
        }],
        ['OS == "mac"', {
          'xcode_settings': {
            'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
            'CLANG_CXX_LANGUAGE_STANDARD': 'c++20',
            'MACOSX_DEPLOYMENT_TARGET': '12.0',
            'OTHER_CPLUSPLUSFLAGS': [
              '-std=c++20',
              '-Wconversion',
              '-Wno-sign-conversion',
            ]
          }
        }],
        ['OS == "win"', {
          'msvs_settings': {
            'VCCLCompilerTool': {
              'AdditionalOptions': ['/std:c++20']
            }
          }
        }]
      ]
    },
  ],

  'conditions': [
    [
      'action_after_build == "true"',
      {
        'targets': [
          {
            'target_name': 'action_after_build',
            'type': 'none',
            'dependencies': ['<(module_name)'],
            'copies': [
              {
                'files': ['<(PRODUCT_DIR)/<(module_name).node'],
                'destination': '<(module_path)'
              }
            ]
          },
        ]
      }
    ]
  ],
}
