import java.util.ArrayList;
import java.util.List;

class Solution {
	int SHEEP = 0;
	int WOLF = 1;
	int maxNum;
	int sheepCount;
	public int solution(int[] info, int[][] edges) {
		Node[] nodes = new Node[info.length];
		sheepCount = 0;
		for(int i = 0; i < info.length; i++) {
			if(info[i] == SHEEP) {
				sheepCount++;
			}
			nodes[i] = new Node(info[i], i);
		}
		for(int i = 0; i<edges.length; i++) {
			nodes[edges[i][0]].addNode(nodes[edges[i][1]]);
		}
		maxNum = 0;
		childNodeSheepAndWolf(nodes[0]);
		findMaxSheepCount(nodes[0], new ArrayList<>(),0, 0, 0);
		// System.out.println(nodes[0]);
		int answer = maxNum;
		return answer;
	}

	public void childNodeSheepAndWolf(Node node) {
		if(node.leftNode != null) {
			childNodeSheepAndWolf(node.leftNode);
			node.lowerSheep += node.leftNode.lowerSheep;
			node.lowerWolf += node.leftNode.lowerWolf;
		}
		if (node.rightNode != null) {
			childNodeSheepAndWolf(node.rightNode);
			node.lowerSheep += node.rightNode.lowerSheep;
			node.lowerWolf += node.rightNode.lowerWolf;
		}
		if(node.wolf == 1) {
			node.lowerWolf++;
		}else {
			node.lowerSheep++;
		}
	}
	public void findMaxSheepCount(Node node, List<Node> visitList, int sheepNum, int wolfNum, int total) {
		// System.out.println(1 + " : " + visitList);
		visitList.remove(node);
		if(node.wolf == SHEEP) {
			sheepNum++;
			total++;
		} else {
			wolfNum++;

		}
        if(wolfNum>=total) {
			total=0;
		}
		maxNum = Math.max(maxNum, total);
		if (node.leftNode != null && node.leftNode.lowerSheep != 0) {
			visitList.add(node.leftNode);
		}
		if (node.rightNode != null && node.rightNode.lowerSheep != 0) {
			visitList.add(node.rightNode);
		}
		if(visitList.isEmpty() && sheepCount == maxNum) {
			// System.out.println(maxNum +" " + total);

			return;
		}
		// System.out.println(2 + " : " + visitList);
		for(int i = 0; i < visitList.size(); i++) {
			findMaxSheepCount(visitList.get(0), visitList, sheepNum, wolfNum, total);
		}
		visitList.add(node);
		visitList.remove(node.rightNode);
		visitList.remove(node.leftNode);
	}
	class Node {
		int wolf;
		int nodeNumber;

		boolean visit = false;
		int lowerSheep = 0;
		int lowerWolf = 0;
		Node parentNode = null;
		Node leftNode = null;
		Node rightNode = null;

		Node(int wolf) {
			this.wolf = wolf;
			// this.nodeNumber = nodeNumber;
		}
		Node(int wolf, int nodeNumber) {
			this.wolf = wolf;
			this.nodeNumber = nodeNumber;
		}

		public void addNode(Node node) {
			node.parentNode = this;
			if(leftNode == null) {
				leftNode = node;
			} else {
				rightNode = node;
			}
		}

		public int getLeftNodeSheepNum() {
			if(leftNode !=null) {
				return leftNode.lowerSheep;
			}
			return 0;
		}
		//동일한 간선에 대한 정보가 중복해서 주어지지 않습니다.
		//항상 하나의 이진 트리 형태로 입력이 주어지며, 잘못된 데이터가 주어지는 경우는 없습니다.

		@Override
		public String toString() {
			return "Node"+ nodeNumber +"{" +
				'}';
		}
	}
}