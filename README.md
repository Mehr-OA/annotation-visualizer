# 📊 Annotation & Knowledge Graph Visualizer

A lightweight, browser-based tool for visualizing Named Entity Recognition (NER) annotations and Knowledge Graph (KG) triples. Built with `D3.js` and Vanilla JavaScript, this tool requires no backend or installation—simply open the HTML file and drop in your JSON data.

## Features

The application is divided into two distinct views accessible via navigation tabs:

### 1. Annotation Viewer (NER)
- Designed to visualize text documents with highlighted entity mentions.

- Text Highlighting: Renders documents with color-coded highlights based on entity types.

- Interactive Tooltips: Hover over entities to view metadata (ID, Type, Confidence score).

- Statistics Dashboard: Displays total phrase counts, unique entity types, and frequency breakdown.

- Data Visualization: Includes a bar chart modal to visualize entity type distribution.

- Dynamic Legends: Automatically generates a color legend based on the entity types found in the uploaded JSON.

### 2. Knowledge Graph Visualizer (KG)

- Designed to visualize relationships (triples) as a force-directed graph using `D3.js`.

- Interactive Controls: Drag nodes to rearrange the graph; Zoom and Pan to explore large networks.

- Auto-Clustering: Nodes are colored by their class/type.

- Tooltips: Hover over nodes to see their label and specific class.

## Getting Started

### Prerequisites

- A web browser (Chrome, Firefox, Edge, Safari).

- An active internet connection (to load the D3.js library via CDN).

### Installation

- Clone this repository or download the visualizer.html file.

- Double-click visualizer.html to open it in your browser.

## Usage

- Using the Annotation Viewer

- Ensure the Annotation Viewer tab is active.

- Drag and drop a compatible `.json` file (see Data Format below) into the "Drag & Drop files" zone, or click the zone to select a file.

- The text will render on the right, with statistics on the left.

- Hover over highlighted text to see details.

- Click "View Charts" to see a frequency bar chart.

## Using the Knowledge Graph

- Click the Knowledge Graph tab.

- Drag and drop a compatible .json file into the floating "KG Data Uploader" box.

- The graph will render automatically.

- Interact:

    - Scroll to zoom in/out.

    - Click & Drag the background to pan.

    - Click & Drag nodes to reposition them.

## Data Formats

## 1. Annotation JSON Structure

The file must contain a sentences array (for the text flow) and an entities array (for global definitions).

Example:
```
{
  "entities": [
    {
      "id": 0,
      "text": "Advanced fluid modeling",
      "type": "G#Modelling",
      "confidence": 1.0
    }
  ],
  "sentences": [
    {
      "text": "Abstract Advanced fluid modeling and PIC/MCC simulations...",
      "entities": [
        {
          "entity_id": 0,
          "start": 1,
          "end": 4,
          "text": "Advanced fluid modeling",
          "type": "G#Modelling"
        }
      ]
    }
  ]
}
```

## 2. Knowledge Graph JSON Structure

The visualizer expects a list of triples.

Important Node Naming Convention:
To utilize the auto-coloring and type detection features, nodes (subject/object) should be formatted as string strings containing a semicolon:

`"Label Text; Entity Type"`

Example:
```
{
  "triples": [
    {
      "subject": "ccrf discharges; Plasma Source",
      "predicate": "usesMedium",
      "object": "helium; Medium"
    },
    {
      "subject": "PIC/MCC simulations; Method",
      "predicate": "measures",
      "object": "rf voltage; Quantity"
    }
  ]
}
```

If no semicolon is found, the type defaults to `"Unknown"`.

## Tech Stack

- HTML5 / CSS3: Custom layout using CSS Grid and Flexbox.

- JavaScript (ES6): Logic for file parsing and DOM manipulation.

- D3.js (v7): Used for rendering the Knowledge Graph SVG.

## License

GNU GENERAL PUBLIC LICENSE Version 3, 29 June 2007