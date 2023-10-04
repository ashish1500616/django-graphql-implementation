import graphene
import graphql_jwt

import links.schema
from hackernews import users
from .users import schema


class Query(
    users.schema.Query,
    links.schema.RelayQuery,
    graphene.ObjectType,
):
    pass


class Mutation(users.schema.Mutation, links.schema.RelayMutation, graphene.ObjectType):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
