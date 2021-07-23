# Toast UI Editor

```bash
# vue에서 사용할 vue-editor 설치
$ npm install --save @toast-ui/vue-editor
$ npm install --save @toast-ui/editor # Latest Version
$ npm install --save @toast-ui/editor@<version> # Specific Version
```

```bash
# 에디터 상에서 코드 하이라이트 기능과 글자 색 기능을 넣기 위한 설치
# toast ui editor 버전이 2.~ 일경우 
$ npm install @toast-ui/editor-plugin-code-syntax-highlight@1.0.0
$ npm install @toast-ui/editor-plugin-color-syntax@1.0.0
```



### create.vue

```vue
<template>
  <div class="editor">
    <button @click="sendData">작성</button>
    <Editor
      ref="toastEditor"
      :value="editorText"
      :options="editorOptions"
      height="400px"
      previewStyle="vertical"
    />
  </div>
</template>

<script>
// Toast UI Editor - Editor
import { Editor } from "@toast-ui/vue-editor";
import "@toast-ui/editor/dist/toastui-editor.css"; // Editor's Style
import "codemirror/lib/codemirror.css";
import "@toast-ui/editor/dist/i18n/ko-kr";


// add dependencies related code-syntax-highlight
import 'highlight.js/styles/github.css';
import hljs from 'highlight.js';
import codeSyntaxHighlight from '@toast-ui/editor-plugin-code-syntax-highlight';

// add dependencies related color-syntax
import 'tui-color-picker/dist/tui-color-picker.css';
import colorSyntax from '@toast-ui/editor-plugin-color-syntax';


const DEFAULT_OPTION = {
  useCommandShortcut: true,
  useDefaultHTMLSanitizer: true,
  usageStatistics: true,
  hideModeSwitch: false,
  plugins: [[codeSyntaxHighlight, { hljs }],colorSyntax]
};

export default {
  name: "markdown4",
  components: {
    Editor,
  },
  data() {
    return {
      editorText: "",
      editorOptions: DEFAULT_OPTION,
    };
  },
  methods: {
    getContent() {
      return this.$refs.toastEditor.invoke('getMarkdown')
    },
    sendData: function() {
      this.$emit('send-data',this.getContent())
    }
  }
};
</script>

<style scoped>
.editor {
  position: absolute;
  /* border: 1px solid black; */
  width: 800px;
  left: 50%;
  transform: translateX(-50%);
  top: 200px;
}
</style>
```



### viewer.vue

```vue
<template>
  <div class="editor">
    <h1>Editor</h1>
    <Editor @send-data="getData"/>
    
    <div style="margin-top: 600px" v-if="viewerText"  >
      <h1>Viewer</h1>
      <Viewer         
      :initialValue="viewerText"
      :options="viewerOptions"/>
    </div>
  </div>
</template>

<script>
// Toast UI Editor - Editor
import "@toast-ui/editor/dist/toastui-editor.css"; // Editor's Style
import "codemirror/lib/codemirror.css";
import "@toast-ui/editor/dist/i18n/ko-kr";


// Toast UI Editor - viewer
import '@toast-ui/editor/dist/toastui-editor-viewer.css';
import { Viewer } from '@toast-ui/vue-editor';

// add dependencies related code-syntax-highlight
import 'highlight.js/styles/github.css';
import hljs from 'highlight.js';
import codeSyntaxHighlight from '@toast-ui/editor-plugin-code-syntax-highlight';

import Editor from '@/views/createArticle/markdown4.vue'


const VIEWER_OPTION = {
  plugins: [[codeSyntaxHighlight, { hljs }]]
}

export default {
  name: "TextEditor",
  components: {
    Viewer,
    Editor,
  },
  data() {
    return {
      viewerText: '',
      viewerOptions: VIEWER_OPTION
    };
  },
  methods: {
    getData: function(data) {
      console.log(data)
      this.viewerText = data
    }
  }
};
</script>

<style scoped>
.editor {
  position: absolute;
  /* border: 1px solid black; */
  width: 800px;
  left: 50%;
  transform: translateX(-50%);
  top: 200px;
}
</style>
```

