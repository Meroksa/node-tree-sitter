{
  "targets": [
    {
      "target_name": "binding",
      "dependencies": [
        "vendor/tree_sitter/tree_sitter.gyp:tree_sitter",
      ],
      "sources": [ "src/binding.cc" ],
      'conditions': [
        ['OS == "mac"', {
          'xcode_settings': {
            'MACOSX_DEPLOYMENT_TARGET': '10.7',
          },
        }]
      ]
    },
  ],
}
