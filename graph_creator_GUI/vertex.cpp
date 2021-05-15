#include "vertex.h"

Vertex::Vertex(QPoint p, int i)
{
    pos = p;
    id = i;
}

void Vertex::addEdge(Vertex v){
    neighbours.push_back(v);
}
