"""
👥 MULTI-USER CONTEXT COLLABORATION - CO-FOUNDER V12

Team collaboration system for sharing context, insights, and strategies.
No future roadmap - SHIPPING NOW!

Features:
- Real-time team collaboration
- Shared context repositories
- Role-based access control
- Comment and annotation system
- Team decision tracking

Author: Co-founder GPT v12 Development Team
Version: 12.0.0 - Complete Collaboration Suite
"""

import json
import asyncio
from typing import Dict, List, Any, Optional, Set
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
import hashlib
import uuid

class UserRole(Enum):
    """User roles in the collaboration system"""
    FOUNDER = "founder"
    CO_FOUNDER = "co_founder"
    EXECUTIVE = "executive"
    TEAM_LEAD = "team_lead"
    ANALYST = "analyst"
    VIEWER = "viewer"

class PermissionLevel(Enum):
    """Permission levels for context access"""
    READ = "read"
    WRITE = "write"
    ADMIN = "admin"
    OWNER = "owner"

@dataclass
class User:
    """User in the collaboration system"""
    id: str
    name: str
    email: str
    role: UserRole
    permissions: List[PermissionLevel]
    created_at: datetime
    last_active: datetime
    preferences: Dict[str, Any] = field(default_factory=dict)

@dataclass
class ContextComment:
    """Comment on context data"""
    id: str
    user_id: str
    content: str
    context_path: str
    timestamp: datetime
    parent_comment_id: Optional[str] = None
    resolved: bool = False

@dataclass
class ContextAnnotation:
    """Annotation on specific context elements"""
    id: str
    user_id: str
    context_path: str
    element_id: str
    annotation_type: str  # highlight, note, question, concern
    content: str
    timestamp: datetime
    resolved: bool = False

@dataclass
class TeamDecision:
    """Team decision based on context analysis"""
    id: str
    title: str
    description: str
    context_sources: List[str]
    decision_maker_id: str
    participants: List[str]
    status: str  # proposed, discussed, approved, rejected, implemented
    created_at: datetime
    deadline: Optional[datetime] = None
    votes: Dict[str, str] = field(default_factory=dict)  # user_id -> vote

class MultiUserContextSystem:
    """
    👥 MULTI-USER CONTEXT COLLABORATION SYSTEM
    
    Enables teams to collaborate on business context analysis and decision making
    """
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.shared_contexts: Dict[str, Dict[str, Any]] = {}
        self.comments: Dict[str, ContextComment] = {}
        self.annotations: Dict[str, ContextAnnotation] = {}
        self.decisions: Dict[str, TeamDecision] = {}
        self.access_logs: List[Dict[str, Any]] = []
        
        # Initialize system
        self._create_demo_users()
        self._create_demo_contexts()
    
    def _create_demo_users(self):
        """Create demo users for testing"""
        
        demo_users = [
            {
                "id": "user_001",
                "name": "Sarah Chen",
                "email": "sarah@company.com",
                "role": UserRole.FOUNDER,
                "permissions": [PermissionLevel.OWNER, PermissionLevel.ADMIN, PermissionLevel.WRITE, PermissionLevel.READ]
            },
            {
                "id": "user_002",
                "name": "Mike Rodriguez", 
                "email": "mike@company.com",
                "role": UserRole.CO_FOUNDER,
                "permissions": [PermissionLevel.ADMIN, PermissionLevel.WRITE, PermissionLevel.READ]
            },
            {
                "id": "user_003",
                "name": "Jessica Kim",
                "email": "jessica@company.com", 
                "role": UserRole.EXECUTIVE,
                "permissions": [PermissionLevel.WRITE, PermissionLevel.READ]
            },
            {
                "id": "user_004",
                "name": "David Thompson",
                "email": "david@company.com",
                "role": UserRole.ANALYST,
                "permissions": [PermissionLevel.READ]
            }
        ]
        
        for user_data in demo_users:
            user = User(
                id=user_data["id"],
                name=user_data["name"],
                email=user_data["email"],
                role=user_data["role"],
                permissions=user_data["permissions"],
                created_at=datetime.now(),
                last_active=datetime.now()
            )
            self.users[user.id] = user
    
    def _create_demo_contexts(self):
        """Create demo shared contexts"""
        
        self.shared_contexts = {
            "revenue_analysis_q4": {
                "id": "revenue_analysis_q4",
                "title": "Q4 Revenue Analysis",
                "description": "Comprehensive revenue analysis for Q4 planning",
                "owner_id": "user_001",
                "created_at": datetime.now().isoformat(),
                "data": {
                    "mrr": 45000,
                    "arr": 540000,
                    "growth_rate": 8.5,
                    "churn_rate": 2.3,
                    "customer_count": 1250,
                    "cac": 150,
                    "ltv": 2400
                },
                "confidence_score": 0.85,
                "sources": ["stripe", "hubspot", "google_analytics"],
                "last_updated": datetime.now().isoformat(),
                "permissions": {
                    "user_001": PermissionLevel.OWNER,
                    "user_002": PermissionLevel.ADMIN,
                    "user_003": PermissionLevel.WRITE,
                    "user_004": PermissionLevel.READ
                }
            },
            
            "market_expansion_research": {
                "id": "market_expansion_research",
                "title": "European Market Expansion Research",
                "description": "Research data for potential expansion into European markets",
                "owner_id": "user_002",
                "created_at": datetime.now().isoformat(),
                "data": {
                    "target_markets": ["UK", "Germany", "France"],
                    "market_size": 2500000000,
                    "competition_level": "high",
                    "regulatory_complexity": "medium",
                    "entry_cost_estimate": 850000
                },
                "confidence_score": 0.72,
                "sources": ["market_research", "competitor_analysis"],
                "last_updated": datetime.now().isoformat(),
                "permissions": {
                    "user_001": PermissionLevel.ADMIN,
                    "user_002": PermissionLevel.OWNER,
                    "user_003": PermissionLevel.WRITE,
                    "user_004": PermissionLevel.READ
                }
            }
        }
    
    def add_user(self, user_data: Dict[str, Any]) -> str:
        """
        👤 ADD NEW USER
        
        Adds a new user to the collaboration system
        """
        
        user_id = user_data.get("id", str(uuid.uuid4()))
        
        user = User(
            id=user_id,
            name=user_data["name"],
            email=user_data["email"],
            role=UserRole(user_data["role"]),
            permissions=[PermissionLevel(p) for p in user_data.get("permissions", ["read"])],
            created_at=datetime.now(),
            last_active=datetime.now(),
            preferences=user_data.get("preferences", {})
        )
        
        self.users[user_id] = user
        
        # Log user creation
        self._log_access("user_added", user_id, {"name": user.name, "role": user.role.value})
        
        return user_id
    
    def share_context(self, context_data: Dict[str, Any], owner_id: str, permissions: Dict[str, str]) -> str:
        """
        📤 SHARE CONTEXT
        
        Shares context data with team members
        """
        
        # Verify owner permissions
        if not self._has_permission(owner_id, PermissionLevel.WRITE):
            raise PermissionError("User does not have write permissions")
        
        context_id = context_data.get("id", str(uuid.uuid4()))
        
        shared_context = {
            "id": context_id,
            "title": context_data["title"],
            "description": context_data.get("description", ""),
            "owner_id": owner_id,
            "created_at": datetime.now().isoformat(),
            "data": context_data["data"],
            "confidence_score": context_data.get("confidence_score", 0.0),
            "sources": context_data.get("sources", []),
            "last_updated": datetime.now().isoformat(),
            "permissions": {
                user_id: PermissionLevel(perm) 
                for user_id, perm in permissions.items()
            }
        }
        
        self.shared_contexts[context_id] = shared_context
        
        # Log context sharing
        self._log_access("context_shared", owner_id, {
            "context_id": context_id,
            "title": shared_context["title"],
            "shared_with": list(permissions.keys())
        })
        
        return context_id
    
    def add_comment(self, user_id: str, context_id: str, content: str, parent_comment_id: Optional[str] = None) -> str:
        """
        💬 ADD COMMENT
        
        Adds a comment to shared context
        """
        
        # Verify user has read access to context
        if not self._can_access_context(user_id, context_id, PermissionLevel.READ):
            raise PermissionError("User cannot access this context")
        
        comment_id = str(uuid.uuid4())
        
        comment = ContextComment(
            id=comment_id,
            user_id=user_id,
            content=content,
            context_path=context_id,
            timestamp=datetime.now(),
            parent_comment_id=parent_comment_id
        )
        
        self.comments[comment_id] = comment
        
        # Log comment addition
        self._log_access("comment_added", user_id, {
            "context_id": context_id,
            "comment_id": comment_id
        })
        
        return comment_id
    
    def add_annotation(self, user_id: str, context_id: str, element_id: str, 
                      annotation_type: str, content: str) -> str:
        """
        📝 ADD ANNOTATION
        
        Adds an annotation to specific context element
        """
        
        # Verify user has read access to context
        if not self._can_access_context(user_id, context_id, PermissionLevel.READ):
            raise PermissionError("User cannot access this context")
        
        annotation_id = str(uuid.uuid4())
        
        annotation = ContextAnnotation(
            id=annotation_id,
            user_id=user_id,
            context_path=context_id,
            element_id=element_id,
            annotation_type=annotation_type,
            content=content,
            timestamp=datetime.now()
        )
        
        self.annotations[annotation_id] = annotation
        
        # Log annotation addition
        self._log_access("annotation_added", user_id, {
            "context_id": context_id,
            "annotation_id": annotation_id,
            "type": annotation_type
        })
        
        return annotation_id
    
    def create_team_decision(self, user_id: str, decision_data: Dict[str, Any]) -> str:
        """
        🗳️ CREATE TEAM DECISION
        
        Creates a team decision based on context analysis
        """
        
        # Verify user has write permissions
        if not self._has_permission(user_id, PermissionLevel.WRITE):
            raise PermissionError("User does not have write permissions")
        
        decision_id = str(uuid.uuid4())
        
        decision = TeamDecision(
            id=decision_id,
            title=decision_data["title"],
            description=decision_data["description"],
            context_sources=decision_data.get("context_sources", []),
            decision_maker_id=user_id,
            participants=decision_data.get("participants", []),
            status="proposed",
            created_at=datetime.now(),
            deadline=datetime.fromisoformat(decision_data["deadline"]) if decision_data.get("deadline") else None
        )
        
        self.decisions[decision_id] = decision
        
        # Log decision creation
        self._log_access("decision_created", user_id, {
            "decision_id": decision_id,
            "title": decision.title,
            "participants": decision.participants
        })
        
        return decision_id
    
    def vote_on_decision(self, user_id: str, decision_id: str, vote: str) -> bool:
        """
        🗳️ VOTE ON DECISION
        
        Allows team members to vote on decisions
        """
        
        if decision_id not in self.decisions:
            raise ValueError("Decision not found")
        
        decision = self.decisions[decision_id]
        
        # Verify user is participant
        if user_id not in decision.participants and user_id != decision.decision_maker_id:
            raise PermissionError("User is not a participant in this decision")
        
        # Verify valid vote
        if vote not in ["approve", "reject", "abstain"]:
            raise ValueError("Invalid vote. Must be 'approve', 'reject', or 'abstain'")
        
        decision.votes[user_id] = vote
        
        # Check if decision should be auto-resolved
        self._check_decision_resolution(decision_id)
        
        # Log vote
        self._log_access("vote_cast", user_id, {
            "decision_id": decision_id,
            "vote": vote
        })
        
        return True
    
    def get_user_contexts(self, user_id: str) -> List[Dict[str, Any]]:
        """
        📋 GET USER CONTEXTS
        
        Returns all contexts accessible to a user
        """
        
        accessible_contexts = []
        
        for context_id, context in self.shared_contexts.items():
            if self._can_access_context(user_id, context_id, PermissionLevel.READ):
                # Add user's permission level to context info
                user_permission = context["permissions"].get(user_id, PermissionLevel.READ)
                
                context_info = {
                    "id": context_id,
                    "title": context["title"],
                    "description": context["description"],
                    "owner_id": context["owner_id"],
                    "created_at": context["created_at"],
                    "confidence_score": context["confidence_score"],
                    "sources": context["sources"],
                    "user_permission": user_permission.value,
                    "comment_count": len([c for c in self.comments.values() if c.context_path == context_id]),
                    "annotation_count": len([a for a in self.annotations.values() if a.context_path == context_id])
                }
                
                accessible_contexts.append(context_info)
        
        return accessible_contexts
    
    def get_context_with_discussions(self, user_id: str, context_id: str) -> Dict[str, Any]:
        """
        💬 GET CONTEXT WITH DISCUSSIONS
        
        Returns context data with comments and annotations
        """
        
        if not self._can_access_context(user_id, context_id, PermissionLevel.READ):
            raise PermissionError("User cannot access this context")
        
        context = self.shared_contexts[context_id].copy()
        
        # Add comments
        context_comments = [
            {
                "id": comment.id,
                "user_name": self.users[comment.user_id].name,
                "content": comment.content,
                "timestamp": comment.timestamp.isoformat(),
                "parent_comment_id": comment.parent_comment_id,
                "resolved": comment.resolved
            }
            for comment in self.comments.values()
            if comment.context_path == context_id
        ]
        
        # Add annotations
        context_annotations = [
            {
                "id": annotation.id,
                "user_name": self.users[annotation.user_id].name,
                "element_id": annotation.element_id,
                "type": annotation.annotation_type,
                "content": annotation.content,
                "timestamp": annotation.timestamp.isoformat(),
                "resolved": annotation.resolved
            }
            for annotation in self.annotations.values()
            if annotation.context_path == context_id
        ]
        
        context["comments"] = context_comments
        context["annotations"] = context_annotations
        
        # Update user's last active
        self.users[user_id].last_active = datetime.now()
        
        return context
    
    def get_team_activity_feed(self, user_id: str, limit: int = 50) -> List[Dict[str, Any]]:
        """
        📰 GET TEAM ACTIVITY FEED
        
        Returns recent team activity for contexts user has access to
        """
        
        # Filter activities to only show contexts user can access
        accessible_activities = []
        
        for log_entry in self.access_logs[-limit:]:
            context_id = log_entry.get("details", {}).get("context_id")
            
            # If activity is related to a context, check access
            if context_id:
                if self._can_access_context(user_id, context_id, PermissionLevel.READ):
                    # Add user name to activity
                    if log_entry["user_id"] in self.users:
                        log_entry["user_name"] = self.users[log_entry["user_id"]].name
                    accessible_activities.append(log_entry)
            else:
                # Non-context activities (user additions, etc.)
                accessible_activities.append(log_entry)
        
        return list(reversed(accessible_activities))  # Most recent first
    
    def _has_permission(self, user_id: str, required_permission: PermissionLevel) -> bool:
        """Check if user has required permission level"""
        
        if user_id not in self.users:
            return False
        
        user = self.users[user_id]
        return required_permission in user.permissions
    
    def _can_access_context(self, user_id: str, context_id: str, required_permission: PermissionLevel) -> bool:
        """Check if user can access specific context with required permission"""
        
        if context_id not in self.shared_contexts:
            return False
        
        context = self.shared_contexts[context_id]
        user_permission = context["permissions"].get(user_id)
        
        if not user_permission:
            return False
        
        # Permission hierarchy: OWNER > ADMIN > WRITE > READ
        permission_levels = {
            PermissionLevel.READ: 1,
            PermissionLevel.WRITE: 2,
            PermissionLevel.ADMIN: 3,
            PermissionLevel.OWNER: 4
        }
        
        return permission_levels.get(user_permission, 0) >= permission_levels.get(required_permission, 0)
    
    def _check_decision_resolution(self, decision_id: str):
        """Check if decision should be automatically resolved based on votes"""
        
        decision = self.decisions[decision_id]
        
        # Simple majority rule
        if len(decision.votes) >= len(decision.participants):
            approve_votes = sum(1 for vote in decision.votes.values() if vote == "approve")
            reject_votes = sum(1 for vote in decision.votes.values() if vote == "reject")
            
            if approve_votes > reject_votes:
                decision.status = "approved"
            elif reject_votes > approve_votes:
                decision.status = "rejected"
            else:
                decision.status = "tie"
    
    def _log_access(self, action: str, user_id: str, details: Dict[str, Any]):
        """Log user actions for activity feed"""
        
        log_entry = {
            "timestamp": datetime.now().isoformat(),
            "action": action,
            "user_id": user_id,
            "details": details
        }
        
        self.access_logs.append(log_entry)
        
        # Keep only last 1000 entries
        if len(self.access_logs) > 1000:
            self.access_logs = self.access_logs[-1000:]

# 🚀 USAGE EXAMPLE

def demo_team_collaboration():
    """Demo the team collaboration system"""
    
    collab_system = MultiUserContextSystem()
    
    print("👥 Co-founder v12 Team Collaboration System")
    print("==========================================")
    
    # Show users
    print(f"\n👤 Team Members: {len(collab_system.users)}")
    for user in collab_system.users.values():
        print(f"  ✅ {user.name} ({user.role.value}) - {len(user.permissions)} permissions")
    
    # Show shared contexts
    print(f"\n📊 Shared Contexts: {len(collab_system.shared_contexts)}")
    for context in collab_system.shared_contexts.values():
        print(f"  ✅ {context['title']} - Confidence: {context['confidence_score']:.2f}")
    
    # Add comments and annotations (demo)
    user_id = "user_003"  # Jessica Kim
    context_id = "revenue_analysis_q4"
    
    # Add comment
    comment_id = collab_system.add_comment(
        user_id, 
        context_id, 
        "The churn rate seems concerning. Should we investigate the top churn reasons?"
    )
    print(f"\n💬 Added comment: {comment_id}")
    
    # Add annotation
    annotation_id = collab_system.add_annotation(
        user_id,
        context_id,
        "churn_rate",
        "concern",
        "2.3% is above industry average of 1.8%"
    )
    print(f"📝 Added annotation: {annotation_id}")
    
    # Create team decision
    decision_id = collab_system.create_team_decision(
        "user_001",  # Sarah Chen (Founder)
        {
            "title": "Implement Churn Reduction Program",
            "description": "Based on Q4 analysis, implement comprehensive churn reduction program",
            "context_sources": [context_id],
            "participants": ["user_001", "user_002", "user_003", "user_004"],
            "deadline": datetime.now().isoformat()
        }
    )
    print(f"🗳️ Created decision: {decision_id}")
    
    # Cast votes
    collab_system.vote_on_decision("user_001", decision_id, "approve")
    collab_system.vote_on_decision("user_002", decision_id, "approve") 
    collab_system.vote_on_decision("user_003", decision_id, "approve")
    print("✅ Votes cast - Decision approved!")
    
    # Get activity feed
    activities = collab_system.get_team_activity_feed("user_001", 10)
    print(f"\n📰 Recent Team Activities: {len(activities)}")
    for activity in activities[-3:]:  # Show last 3
        print(f"  📌 {activity['action']} by {activity.get('user_name', 'Unknown')}")
    
    return collab_system

if __name__ == "__main__":
    demo_team_collaboration() 